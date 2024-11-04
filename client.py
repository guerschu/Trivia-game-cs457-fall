import sys
import socket
import selectors
import traceback
import time
import splash
import libclient

selVar = selectors.DefaultSelector()
# messageClient = [b"Got it to work, testing connection", b" Message 2 Ready To Play Game?"]

def waitUser():
    splash.options()
    while True:
        user_input = input("Enter your input (type 'exit' to quit): ")
        if user_input == "exit":
            return user_input
        
        
def startConnectionClient(host, port, requests, name):
    server_addres = (host, port)
    print("Starting the connection to", server_addres)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addres)
    event = selectors.EVENT_READ | selectors.EVENT_WRITE
    messageClient = libclient.Message(selVar, sock, server_addres, requests, name)
    selVar.register(sock, event, data=messageClient)
        
#this should be triggered when it is a read or wirte event, making sure it actually does them


def createRequest(action, value):
    if action == "trivia":
        return dict(
            type="text/json",
            encoding="UTF-8",
            content=dict(action=action, value=value),
        )
    else:
        print("Not Allowed Yet, Please Try Again")

# the main part of the program we will be using

if len(sys.argv) != 6:
    print("usage:", sys.argv[0], "<host> <port> <action> <value> <name>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
action, value = sys.argv[3], sys.argv[4]
clientName = sys.argv[5] # added to identify the different  clients
request = createRequest(action, value)

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
        # if eventTest:
        #     for key, mask, in eventTest:
        #         ServiceConnectClient(key, mask)
        if not selVar.get_map():
            break
except KeyboardInterrupt:
    print("Caught keyboard interruption, exiting, User terminated program")
finally:
    selVar.close()
