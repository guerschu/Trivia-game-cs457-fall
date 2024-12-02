import sys
import socket
import selectors
import traceback
import time
import splash
import libclient

selVar = selectors.DefaultSelector()
# messageClient = [b"Got it to work, testing connection", b" Message 2 Ready To Play Game?"]
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
        
        
def startConnectionClient(host, port, requests, name):
    server_addres = (host, port)
    print("Starting the connection to", server_addres)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addres)
    event = selectors.EVENT_READ | selectors.EVENT_WRITE
    messageClient = libclient.Message(selVar, sock, server_addres, requests, name)
    selVar.register(sock, event, data=messageClient)
        
#this should be triggered when it is a read or write event, making sure it actually does them


def createRequest(category):
    return dict(
        type="text/json",
        encoding="UTF-8",
        content=dict(category=category)
    )

# the main part of the program we will be using

if len(sys.argv) != 5 or sys.argv[1] != "-i" or sys.argv[3] != "-p":
    print("usage:", sys.argv[0], "-i <SERVER_IP/DNS> -p <PORT>")
    sys.exit(1)


splash.home()
time.sleep(3)
#<action> <value> <name>

host, port = sys.argv[2], int(sys.argv[4])
category = waitUserRequest()
splash.userName()
clientName = input("Enter your input (type 'exit' to quit): ")
request = createRequest(category)
print(f"Attempting to connect {clientName} to {host} on port: {port}...")
startConnectionClient(host, port, request, clientName)

try:
    while True:
        eventTest = selVar.select(timeout=1)
        for key, mask in eventTest:
            messageClient = key.data
            try:
                print("Sent message to clinetlib")
                messageClient.process_events(mask)
            except Exception:
                print(
                    f"Main: Error: Exception for {messageClient.addr}:\n"
                    f"{traceback.format_exc()}"
                )
                messageClient.close()
        if not selVar.get_map():
            break
except KeyboardInterrupt:
    print("Caught keyboard interruption, exiting, User terminated program")
finally:
    selVar.close()
