import sys
import socket
import selectors
import types


selVar = selectors.DefaultSelector()
messageClient = [b"Got it to work, testing connection", b"Message 2 Ready To Play Game?"]

def startConnectionClient(host, port, num_conns):
    server_addres = (host, port)
    for i in range(0, num_conns):
        connectionNum = i+1
        print("Starting the connection", connectionNum, "to", server_addres)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addres)
        event = selectors.EVENT_READ | selectors.EVENT_WRITE
        dataEntre = types.SimpleNamespace(connectionNum = connectionNum,
            msgTotal=sum(len(m) for m in messageClient),
            recvTotal=0,
            messageClient=list(messageClient),
            outB=b"",
        )
        selVar.register(sock, event, data=dataEntre)
        
#this should be triggered when it is a read or wirte event, making sure it actually does them
def ServiceConnectClient(key, mask):
    sock = key.fileobj
    dataEntre = key.data
    if mask & selectors.EVENT_READ:
        recvData = sock.recv(1024) # makes it able to read
        if recvData:
            print("Recieved", repr(recvData), "from the connection", dataEntre.connectionNum)
            dataEntre.recvTotal += len(recvData)
            if not recvData or dataEntre.recvTotal == dataEntre.msgTotal:
                print("Closing the Connection", dataEntre.connectionNum)
                selVar.unregister(sock)
                sock.close()
    if mask & selectors.EVENT_WRITE:
        if not dataEntre.outB and dataEntre.messageClient:
            dataEntre.outB = dataEntre.messageClient.pop(0)
        if dataEntre.outB:
            print("Sending", repr(dataEntre.outB), "to Connection", dataEntre.connectionNum)
            sent = sock.send(dataEntre.outB)  # Should be ready to write
            dataEntre.outB = dataEntre.outB[sent:]

# the main part of the program we will be using

host = '127.0.0.1' # this is 0.0.0.0 to be able to communicate across machines
port = 49000

numConns = 10

startConnectionClient(host, port, numConns)

try:
    while True:
        eventTest = selVar.select(timeout=1)
        if eventTest:
            for key, mask, in eventTest:
                ServiceConnectClient(key, mask)
        if not selVar.get_map():
            break
except KeyboardInterrupt:
    print("Caught keyboard interruption, exiting, User terminated program")
finally:
    selVar.close()
