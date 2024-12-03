import sys
import socket
import time
import splash
import libclient

validOptions = ["animal","exit","history","locations","location"]

def waitUserRequest():
    splash.options()
    while True:
        user_input = input("Enter your input (type 'exit' to quit): ").lower()
        if user_input == "exit" or user_input == 'x':
            sys.exit(1)
        if user_input in validOptions:
            splash.youChose(user_input)
            return user_input.lower()
        else:
            print(print('''|  Choose a valid option and try again   |'''))

# the main part of the program we will be using

if len(sys.argv) != 5 or sys.argv[1] != "-i" or sys.argv[3] != "-p":
    print("usage:", sys.argv[0], "-i <SERVER_IP/DNS> -p <PORT>")
    sys.exit(1)


splash.home()
#time.sleep(3)
#<action> <value> <name>

host, port = sys.argv[2], int(sys.argv[4])
category = waitUserRequest()
splash.userName()
clientName = input("Type your username (type 'exit' to quit): ")
print(f"Attempting to connect {clientName} to {host} on port: {port}...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
#client.setblocking(False)

def send(message):
    message = message.encode('utf-8')
    msg_len = len(message)
    share_len = str(msg_len).encode('utf-8')
    share_len += b' ' * (64-len(share_len))
    client.send(share_len)
    client.send(message)

def start(usr_name):
    print(f"Game started for {usr_name}")
    #implement here what the server is sending back and all that
    try:
        send(usr_name)
        while True:
            msg_len = client.recv(64).decode('utf-8')
            if msg_len:
                msg_len = int(msg_len)
                message = client.recv(msg_len).decode('utf-8')
                if message == "DISCON":
                    break
                print(f"Server: {message}")
                #if meeting proper conditons about game ask for user input to send
    except KeyboardInterrupt:
        print("You interrupted your game! Disconnecting...")
        send("DISCON")
        client.close()

start(clientName)
