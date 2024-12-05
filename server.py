import socket
import sys
import custom_logger as log
import threading
import splash

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
        "Name": "admin"
        }
    },
    "history": {
        "admin": {
        "IP":"0.0.0.0",
        "GP":-1,
        "SEL":"giraffe",
        "Name": "admin"
        }
    },
    "locations": {
        "admin": {
        "IP":"0.0.0.0",
        "GP":-1,
        "SEL":"giraffe",
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

def validate(conn, user_input):
    if user_input == "exit" or user_input == 'x':
        send(conn, "Disconnecting you Goodbye...")
        return False
    if user_input.lower() in validOptions:
        send(conn, splash.youChose(user_input))
        return True
    else:
        send(conn, "!|  Choose a valid option and try again   |")
        return False

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

def send(conn, message):
    message = message.encode('utf-8')
    msg_len = len(message)
    share_len = str(msg_len).encode('utf-8')
    share_len += b' ' * (64-len(share_len))
    conn.send(share_len)
    conn.send(message)

def serve_client(conn, addr):
    log.logIt(f"Connection from client at: {addr} with chosen name: ")
    send(conn,"!"+splash.userName())
    send(conn,"!"+splash.options())
    usrn = ""
    setup = 0 # 0 means needs username, 1 means needs selection, 2 means all set up
    inlobby = False
    while not inlobby:
        msg_len = conn.recv(64).decode('utf-8')
        if msg_len:
            msg_len = int(msg_len)
            message = conn.recv(msg_len).decode('utf-8')
            if message == "DISCON":
                update_conns()
                remove_player(usrn)
                break
            if message[0] == "!":
                if setup == 0:
                    usrn = message[1:]
                    #print(usrn)
                    players[usrn] = {"IP":addr[0],"GP":0,"SEL":"", "Done": False, "Name": usrn}
                    setup += 1
                    send(conn, splash.youChose(message[1:]))
                elif setup == 1:
                    if validate(conn, message[1:]):
                        players[usrn].update({"SEL": (message[1:].lower())})
                        print(players[usrn]["Name"] + " Selected Category "+ message[1:])
                        log.logIt(players[usrn]["Name"] + " Selected Category "+ message[1:])
                        lobby[players[usrn]["SEL"]][usrn] = players[usrn]
                        update_lobby(players[usrn]["SEL"])
                        inlobby = True
            log.logIt(f"Client at addr says: {message}")
    #print(players)
    selection = players[usrn]["SEL"]
    send(conn, splash.waiting())
    while True:
        if lobby_status(selection):
            for i, func in Questions[selection].items():
                player_name = players[usrn]["Name"]
                try:
                    if player_name == usrn:
                        print(f"{player_name} : got question {i}")
                        log.logIt(f"{player_name} : got question {i}")
                except KeyError:
                    print(f"KeyError: 'Name' not found for user {usrn}")
                    send(conn, "An error occurred. Please try again.")
                send(conn, "!" + func())
                msg_len = conn.recv(64).decode('utf-8')
                if msg_len:
                    msg_len = int(msg_len)
                    message = conn.recv(msg_len).decode('utf-8')
                    try:
                        if player_name == usrn:
                            print(f"{player_name} Answered: {i} with {message[1:]}")
                            log.logIt(f"{player_name} Answered: {i} with {message[1:]}")
                    except KeyError as e:
                        log.logIt(f"KeyError: {e}")
                        send(conn, "An error occurred. Please try again. Happened with the Lobby accessing a Name")
                        break
                    if message == "DISCON":
                        update_conns()
                        remove_player(usrn)
                        break
                    if message[1:] == Answers[selection][i]:
                        players[usrn].update({"GP": players[usrn]["GP"] + 1})
                        print(f"{player_name} Got It Correct!")
                        log.logIt(f"{player_name} Got It Correct!")
                        send(conn, splash.correct())
                    elif message[1:] in ['A', 'B', 'C']:
                        print(f"{player_name} Got It Wrong! Womp Womp")
                        log.logIt(f"{player_name} Got It Wrong! Womp Womp")
                        send(conn, splash.wrong())
                    else:
                        incorrecInput = False
                        while incorrecInput:
                            send(conn, "Incorrect Input Type")
                            send(conn, "!"+func())
                            msg_len = conn.recv(64).decode('utf-8')
                            if msg_len:
                                msg_len = int(msg_len)
                                message = conn.recv(msg_len).decode('utf-8')
                                try:
                                    if player_name == usrn:
                                        print(f"{player_name} Answered: {i} with {message[1:]}")
                                        log.logIt(f"{player_name} Answered: {i} with {message[1:]}")
                                except KeyError as e:
                                    log.logIt(f"KeyError: {e}")
                                    send(conn, "An error occurred. Please try again. Happened with the Lobby accessing a Name")
                                    break
                                if message == "DISCON":
                                    update_conns()
                                    remove_player(usrn)
                                    break
                                if message[1:] == Answers[selection][i]:
                                    players[usrn].update({"GP": players[usrn]["GP"] + 1})
                                    print(f"{player_name} Got It Correct!")
                                    log.logIt(f"{player_name} Got It Correct!")
                                    send(conn, splash.correct())
                                    break
                                elif message[1:] in ['A', 'B', 'C']:
                                    print(f"{player_name} Got It Wrong! Womp Womp")
                                    log.logIt(f"{player_name} Got It Wrong! Womp Womp")
                                    send(conn, splash.wrong())
                                    break
            send(conn, splash.scoreBoard(players))
            if i > 6:
                break
        
    send(conn, splash.winCondition(lobby[selection]))
    send(conn, splash.thanksForPlaying())
    send(conn, "DISCON")
    remove_player(usrn)
    conn.close()
    

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