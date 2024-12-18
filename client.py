import sys
import socket
import splash
import custom_logger as log

# the main part of the program we will be using

if len(sys.argv) != 5 or sys.argv[1] != "-i" or sys.argv[3] != "-p":
    print("usage:", sys.argv[0], "-i <SERVER_IP/DNS> -p <PORT>")
    sys.exit(1)


splash.home()
#time.sleep(3)
#<action> <value> <name>

host, port = sys.argv[2], int(sys.argv[4])
print(f"Attempting to connect to {host} on port: {port}...")
log.logIt(f"Attempting to connect to {host} on port: {port}...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
#client.setblocking(False)

def send(message):
    message = message.encode('utf-8')
    msg_len = len(message)
    share_len = str(msg_len).encode('utf-8')
    share_len += b' ' * (64-len(share_len))
    client.send(share_len)
    client.send(message)

def start():
    #implement here what the server is sending back and all that
    try:
        print(splash.home())
        while True:
            msg_len = client.recv(64).decode('utf-8')
            if msg_len:
                msg_len = int(msg_len)
                message = client.recv(msg_len).decode('utf-8')
                if message == "DISCON":
                    break
                if message[0] == "!":
                    print(f"Server: {message}")
                    log.logIt(f"Client got message from Server: {message}")
                    send("!"+input("Response: "))
                print(f"Server: {message}")
                log.logIt(f"Client got another message from Server: {message}")
                #if meeting proper conditons about game ask for user input to send
    except KeyboardInterrupt:
        print("You interrupted your game! Disconnecting...")
        send("DISCON")
        log.logIt("Client Disconnected from KeyBoard")
        client.close()

start()
