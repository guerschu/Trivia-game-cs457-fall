import selectors
import socket
import types
import sys
sel = selectors.DefaultSelector()

# accept wrapper routine, when lSocket gets request to connect

def acceptWrapper(newSocket):
    conn, addr = newSocket.accept()
    print("Connection from client at: ", addr)
    conn.setblocking(False)
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


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Avoid bind() exception: OSError: [Errno 48] Address already in use
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
                acceptWrapper(key.fileobj)
            else:
                serviceClient(key, mask)
except KeyboardInterrupt:
    print("Service interupted by admin, exiting...")
finally:
    sel.close()
