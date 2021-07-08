import socket

HEADER = 64
PORT = 5050
FMT = 'utf-8'
DISCONNECT_MSG = "[DISCONNECED]"

SERVER = '192.168.1.195'
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FMT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FMT)
    send_length += b' '* (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FMT))


send("Hello World")