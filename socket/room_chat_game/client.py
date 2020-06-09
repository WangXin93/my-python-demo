import socket
import select
import sys

IP_ADDRESS = socket.gethostname()
PORT = 5556
HEADER_LENGTH = 10
ROOM_LENGTH = 10
ROOM = '233'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP_ADDRESS, PORT))

room = f"{ROOM:<{ROOM_LENGTH}}"
server.send(room.encode())

while True:
    """ Maintain a list of possible input stream."""
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message.decode())
        else:
            message = sys.stdin.readline()
            message_header = f"{len(message):<{HEADER_LENGTH}}"
            room = f"{ROOM:<{ROOM_LENGTH}}"
            server.send(
                message_header.encode() + room.encode() + message.encode())
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
