import selectors
import socket
import types
sel = selectors.DefaultSelector()

# accept wrapper routine, when lSocket gets request to connect

def acceptWrapper(newSocket):
    conn, addr = newSocket.accept()
    print("Connection from client at: ", addr)
    conn.setBlocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


# subroutine to service client for read or write

def serviceClient(key, mask):
    workSocket = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recvData = workSocket.recv(1024) #sets up to read
        if recvData:
            data.outb += recvData
        else:
            print("Ending connection to: ", data.addr)
            sel.unregister(workSocket)
            workSocket.close()
    else:
        if data.outb:
            print("Echoing to client: ", repr(data.outb), "client is: ", data.addr)
            sent = workSocket.send(data.outb) #sets up to write
            data.outb = data.outb[sent:]


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
