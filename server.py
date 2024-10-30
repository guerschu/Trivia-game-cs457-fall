
import selectors
import socket
import types
import sys
import libserver

sel = selectors.DefaultSelector()

# accept wrapper routine, when lSocket gets request to connect

def acceptWrapper(sock):
    conn, addr = sock.accept()
    print("Connection from client at: ", addr, " with chosen name: ")
    conn.setblocking(False)
    message = libserver.Message(sel, conn, addr)
    sel.register(conn, selectors.EVENT_READ, data=message)


# subroutine to service client for read or write

#program starts here
if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Avoid bind() exception: OSError: [Errno 48] Address already in use
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# lSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host,port))
lsock.listen()

print("Server running on: ",host,", Listening on: ",port)
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)


# while waiting for comms from client
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                acceptWrapper(key.fileobj)
            else:
                message = key.data
                try:
                    message.process_events(mask)
                except Exception:
                    print(
                        f"Main: Error: Exception for {message.addr}:\n"
                    )
                    message.close()

except KeyboardInterrupt:
    print("Service interupted by admin, exiting...")
finally:
    sel.close()
