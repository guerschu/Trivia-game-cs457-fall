import sys
import socket
import selectors
import traceback

import libclient

selVar = selectors.DefaultSelector()
# messageClient = [b"Got it to work, testing connection", b" Message 2 Ready To Play Game?"]

def startConnectionClient(host, port, requests):
    server_addres = (host, port)
    print("Starting the connection to", server_addres)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addres)
    event = selectors.EVENT_READ | selectors.EVENT_WRITE
    messageClient = libclient.Messages(selVar, sock, server_addres, requests)
    selVar.register(sock, event, data=messageClient)
        
#this should be triggered when it is a read or wirte event, making sure it actually does them


def createRequest(action, value):
    if action == "animal":
        return dict(
            type="text/json",
            encoding="uft-8",
            context=dict(action=action, value=value),
        )
    else:
        print("Not Allowed Yet, Please Try Again")

# the main part of the program we will be using

if len(sys.argv) != 5:
    print("usage:", sys.argv[0], "<host> <port> <action> <value>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
action, value = sys.argv[3], sys.argv[4]
request = createRequest(action, value)

startConnectionClient(host, port, request)

try:
    while True:
        eventTest = selVar.select(timeout=1)
        for key, mask in eventTest:
            messageClient = key.data
            try:
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
