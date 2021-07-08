import socket
import threading


HEADER = 64
PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)


FMT = 'utf-8'
DISCONNECT_MSG = "[DISCONNECED]"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FMT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FMT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f'[{addr}]: {msg}')
            conn.send("Message Received...".encode(FMT))

    conn.close()



def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONENCTIONS] {threading.active_count() - 1}')
        


print("[STARTING] Server is starting...")
start()

