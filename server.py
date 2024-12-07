import socket
import sys
import custom_logger as log
import threading
import splash
import time

players = {
    "admin": {
        "IP":"0.0.0.0",
        "GP":-1,
        "SEL":"giraffe",
        "Done": False,
        "Name": "admin"
        }
}

lobby = {
    "animal": {
        "admin": {
        "IP":"0.0.0.0",
        "GP":-1,
        "SEL":"giraffe",
        "Done": False,
        "Name": "admin"
        }
    },
    "history": {
        "admin": {
        "IP":"0.0.0.0",
        "GP":-1,
        "SEL":"giraffe",
        "Done": False,
        "Name": "admin"
        }
    },
    "locations": {
        "admin": {
        "IP":"0.0.0.0",
        "GP":-1,
        "SEL":"giraffe",
        "Done": False,
        "Name": "admin"
        }
    }
}

status = {
    "animal": {
        "val": False,
        "E": False
    },
    "history": {
        "val": False,
        "E": False
    },
    "locations": {
        "val": False,
        "E": False
    }
}

Answers = {
    "animal": {"1": "A", "2": "B", "3": "A", "4": "A", "5": "C", "6": "B"},
    "history": {"1": "A", "2": "B", "3": "B", "4": "C", "5": "A", "6": "B"},
    "locations": {"1": "A", "2": "B", "3": "A", "4": "A", "5": " B", "6": "C"}
}

Questions ={
    "animal": {"1": splash.animal_question0, "2": splash.animal_question1, "3": splash.animal_question2, "4": splash.animal_question3, "5": splash.animal_question4, "6": splash.animal_question5},
    "history": {"1": splash.history_questions0, "2": splash.history_questions1, "3": splash.history_questions2, "4": splash.history_questions3, "5": splash.history_questions4, "6": splash.history_questions5},
    "locations": {"1": splash.location_questions0, "2": splash.location_questions1, "3": splash.location_questions2, "4": splash.location_questions3, "5": splash.location_questions4, "6":splash.location_questions5}
}

#program starts here
if len(sys.argv) != 3 or sys.argv[1] != "-p":
    print("usage:", sys.argv[0], "-p <PORT>")
    sys.exit(1)

port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

validOptions = ["animal","exit","history","location"]


def update_conns():
    strcur = f"Current connections: {threading.active_count() - 1}"
    log.logIt(strcur)
    print(strcur)

def start_lobby(lobby_name):
    status[lobby_name]["val"] = True

def lobby_status(lobby_name):
    return status[lobby_name]["val"]

def update_lobby(lobby_name):
    if (not lobby_status(lobby_name)) and (len(lobby[lobby_name]) >= 3):
        start_lobby(lobby_name)

def remove_player(name):
    if(players[name]["SEL"] != ""):
        del lobby[players[name]["SEL"]][name]
    del players[name]

def create_user(conn, addr, usrn):
    #print(usrn)
    players[usrn] = {"IP":addr[0],"GP":0,"SEL":"", "Done": False, "Name": usrn}
    log.logIt(f"User {usrn} added to current players")
    return usrn

def send_recieve(conn, sent_list):
    responses = []
    for i in sent_list:
        send(conn, i)
        msg_len = conn.recv(64).decode('utf-8')
        if(msg_len):
            msg_len = int(msg_len)
            message = conn.recv(msg_len).decode('utf-8')
            if message == "DISCON":
                break
                #gracefully handle exit of client
            elif message[0] == "!":
                responses.append(message[1:])
    return responses

def validate(conn, user_input):
    while True:
        if user_input != "" and user_input.lower() in validOptions:
            send(conn, splash.youChose(user_input))
            return user_input
        else:
            user_input = send_recieve(conn, ["!"+splash.options()+"\n|  Choose a valid option and try again   |"])[0]

def await_lobby(selection):
    while not lobby_status(selection):
        pass
    pass

def player_into_lobby(conn, addr, usrn, selection):
    selection = validate(conn, selection)
    print("Here?")
    players[usrn].update({"SEL": (selection.lower())})
    print(players[usrn]["Name"] + " Selected Category "+ selection)
    log.logIt(players[usrn]["Name"] + " Selected Category "+ selection)
    lobby[players[usrn]["SEL"]][usrn] = players[usrn]
    update_lobby(players[usrn]["SEL"])

def send(conn, message):
    message = message.encode('utf-8')
    msg_len = len(message)
    share_len = str(msg_len).encode('utf-8')
    share_len += b' ' * (64-len(share_len))
    conn.send(share_len)
    conn.send(message)

def serve_client(conn, addr):
    log.logIt(f"Connection from client at: {addr} with chosen name: ")
    need_info = ["!"+splash.userName(),"!"+splash.options()]
    usrn = send_recieve(conn, [need_info[0]])[0]
    send(conn, splash.youChose(usrn))
    create_user(conn, addr, usrn)
    while True:
        player_into_lobby(conn, addr, usrn, send_recieve(conn, [need_info[1]])[0])
        #print(players)
        selection = players[usrn]["SEL"]
        send(conn, splash.waiting())
        await_lobby(selection)
        if serve_client_lobby(conn, addr, usrn, selection):
            #select lobby/options operation
            pass
        else:
            #disconnect user operations
            send(conn, splash.thanksForPlaying())
            send(conn, "DISCON")
            remove_player(usrn)
            conn.close()
            break

def validate_answer(ans, conn):
    while True:
        if ans not in ["A", "B", "C"]:
            ans = send_recieve(conn, ["!Please make sure your answer is A, B or C"])[0]
        else:
            return ans

def check_answer(usrn, ans, selection, map, conn):
    if Answers[selection][map] == ans:
        lobby[selection][usrn].update({"GP": lobby[selection][usrn]["GP"] + 1})
        send(conn, splash.correct())
    else:
        send(conn, splash.wrong())

def await_others(selection):
    start_time = time.time()
    everyone_done = False
    while not everyone_done:
        if (start_time - time.time() >= 10): #incase anyone false behind the game doesnt hang
            break
        for player in list(lobby[selection].keys()):
            everyone_done = players[player]["Done"]

def play_again(conn):
    ans = send_recieve(conn, ["!"+"Play again? y or n"])[0]
    while True:
        if ans.lower() not in ["y","n","yes","no"]:
            ans = send_recieve(conn, ["!Please make sure your answer is y or n"])[0]
        else:
            return True

def serve_client_lobby(conn, addr, usrn, selection):
    print("Player is playing")
    for i, func in Questions[selection].items():
        print(i)
        send(conn, func())#Give user a question
        print("Sent question")
        ans = validate_answer(send_recieve(conn, ["!"+i])[0], conn) #gather answer
        lobby[selection][usrn].update({"Done": True})
        print("Gathered answer")
        await_others(selection) #Wait for all users in lobby to answer to move on, if this player hasn't answered -> idk what to do with this special case
        print("done awaiting")
        check_answer(usrn, ans, selection, i, conn) #Check answer
        print("checked answer")
        send(conn, splash.scoreBoard(lobby[selection])) #Print scoreboard
        print("Sent scores")
        lobby[selection][usrn].update({"Done": False}) #reset all users in lobby flag
    send(conn, splash.winCondition(lobby[selection]))
    #repeat for all questions
    return play_again(conn)


def run_server():
    try:
        server.listen()  # Maximum number of clients to queue
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=serve_client, args=(conn, addr))
            thread.start()
            strcur = f"Current connections: {threading.active_count() - 1} from IP {addr[0]}"
            log.logIt(strcur)
            print(strcur + " From " + addr[0])
    except KeyboardInterrupt:
        print("Service interupted by admin, exiting...")

server.bind(('0.0.0.0', port))  # Listen on all interfaces
print("Server running on: 0.0.0.0, Listening on:", port)

#usage: {IP,POINTS,SUGGESTION}
run_server()
# server.setblocking(False)  # Make it non-blocking