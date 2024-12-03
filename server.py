import socket
import sys
import custom_logger as log
import threading


#program starts here
if len(sys.argv) != 3 or sys.argv[1] != "-p":
    print("usage:", sys.argv[0], "-p <PORT>")
    sys.exit(1)

port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def update_conns():
    strcur = f"Current connections: {threading.activeCount() - 1}"
    log.logIt(strcur)
    print(strcur)

def send(conn, message):
    message = message.encode('utf-8')
    msg_len = len(message)
    share_len = str(msg_len).encode('utf-8')
    share_len += b' ' * (64-len(share_len))
    conn.send(share_len)
    conn.send(message)

def serve_client(conn, addr):
    log.logIt(f"Connection from client at: {addr} with chosen name: ")

    while True:
        msg_len = conn.recv(64).decode('utf-8')
        if msg_len:
            msg_len = int(msg_len)
            message = conn.recv(msg_len).decode('utf-8')
            if message == "DISCON":
                update_conns()
                break
            log.logIt(f"Client at addr says: {message}")
            send(conn, "Server: we hear you!")
    conn.close()

def run_server():
    try:
        server.listen()  # Maximum number of clients to queue
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=serve_client, args=(conn, addr))
            thread.start()
            strcur = f"Current connections: {threading.activeCount() - 1}"
            log.logIt(strcur)
            print(strcur)
    except KeyboardInterrupt:
        print("Service interupted by admin, exiting...")

server.bind(('0.0.0.0', port))  # Listen on all interfaces
print("Server running on: 0.0.0.0, Listening on:", port)
players = {
    "admin": {"IP":"0.0.0.0","GP":-1,"SEL":"giraffe"}
} 
#usage: {IP,POINTS,SUGGESTION}
run_server()
# server.setblocking(False)  # Make it non-blocking