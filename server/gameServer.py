import selectors
import socket
sel = selectors.DefaultSelector()

# main server program
host = '0.0.0.0'
port = 60001 # 60000 + 1 for pizzaz -mallory

#listening socket to register with SELECT

lSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lSocket.bind((host,port))
lSocket.listen()

print("Server running on: ",host,", Listening on: ",port)
lSocket.setblocking(False)
sel.register(lSocket, selectors.EVENT_READ, data=None)


# while waiting for comms from client
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                # implment accecptWrapper
                print("Accept")
            else:
                # implement service connection
                print("service")
except KeyboardInterrupt:
    print("Service interupted by admin, exiting...")
finally:
    sel.close()
