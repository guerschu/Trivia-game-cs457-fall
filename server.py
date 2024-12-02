
import selectors
import socket
import types
import sys
import libserver
import custom_logger as log
sel = selectors.DefaultSelector()

# accept wrapper routine, when lSocket gets request to connect

def acceptWrapper(sock):
    conn, addr = sock.accept()
    logConn = f"Connection from client at:  {addr} with chosen name: "
    conn.setblocking(False)
    message = libserver.Message(sel, conn, addr)
    sel.register(conn, selectors.EVENT_READ, data=message)
    log.logIt(logConn)

def serviceConnection(message, mask):
    try:
        message.process_events(mask)
    except Exception as e:
        print(f"Error processing events for {message.addr}: {e}")
        message.close()
# subroutine to service client for read or write

#program starts here
if len(sys.argv) != 3 or sys.argv[1] != "-p":
    print("usage:", sys.argv[0], "-p <PORT>")
    sys.exit(1)

port = int(sys.argv[2])

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind(('0.0.0.0', port))  # Listen on all interfaces
lsock.listen(100)  # Maximum number of clients to queue
lsock.setblocking(False)  # Make it non-blocking


lsock.setblocking(False)

if not any(key.fileobj == lsock for key in sel.get_map().values()):
    sel.register(lsock, selectors.EVENT_READ, data=None)
    print("Server running on: 0.0.0.0, Listening on:", port)
else:
    print(f"Warning: Listening socket is already registered!")


# while waiting for comms from client
try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                acceptWrapper(key.fileobj)
            else:
                message = key.data
                serviceConnection(message, mask)
                try:
                    message.process_events(mask)
                except Exception:
                    print(f"Main: Error: Exception for {message.addr}:\n")
                    message.close()

except KeyboardInterrupt:
    print("Service interupted by admin, exiting...")
finally:
    sel.close()
