import sys
import socket
import selectors
import types


selectorsVar = selectors.DefaultSelector()
message = [b"Got it to work, testing connection", b"Message 2 Ready To Play Game?"]

def startConnectionClient(host, port, num_conns):
    server_addres = (host, ports)
    for i in range(0, num_conns):
        connectionNum = i+1
        print("Starting the connection", connectionNum, "to", server_addres)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(false)
        sock.connect_ex(server_addres)
        event = selectors.EVENT_READ | selectors.EVENT_WRITE
        dataEntre = types.SimpleNamespace(
            connectionNum = connectionNum
            msgTotal=sum(len(m) for m in messageClient),
            recvTotal=0,
            messageClient=list(messageClient),
            outB=b"",
        )
        selVar.register(sock, events, dataVar=dataVar)

#this should be triggered when it is a read or wirte event, making sure it actually does them
def ServiceConnectClient(key, mask):
    sock = key.fileobj
    dataEntre = key.data
    if mask & selectors.EVENT_READ:
        recvData = sock.recv(1024) # makes it able to read
        if recvData:
            print("Recieved", repr(recvData), "from the connection", dataEntre.connectionNum)
            dataEntre.recv_total += len(recvData)
            if not recvData or dataEntre.recv_total == dataEntre.msg_total:
                print("Closing the Connection", dataEntre.connectionNum)
                selVar.unregistered(sock)
                sock.close()
    if mask & selectors.EVENT_WRITE:
        if not dataEntre.outb and dataEntre.messages:
            dataEntre.outb = dataEntre.messages.pop(0)
        if dataEntre.outb:
            print("Sending", repr(dataEntre.outb), "to Connection", dataEntre.connectionNum)
            sent = sock.send(dataEntre.outb)  # Should be ready to write
            dataEntre.outb = dataEntre.outb[sent:]

# the main part of the program we will be using

host = '0.0.0.0' # this is 0.0.0.0 to be able to communicate across machines
port = 6001
numConns = 10

startConnectionClient(host, port, numConns)

try:
    while true:
        eventTest = selVar.select(timeout=1)
        if eventTest:
            for key, mask, in eventTest:
                ServiceConnectClient(key, mask)
        if not selVar.get_map():
            break
exept Keyboardinterrupt:
    print("Caught keyboard interruption, exiting, User terminated program")
finally:
    selVar.close()
