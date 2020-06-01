"""
* Sockets are interior endopoints built for sending and receiving data
* A single network will have two sockets
* Sockets are a combination of an IP address and a Port
"""
import socket

# IP_ADDRESS = "127.0.0.1"
IP_ADDRESS = socket.gethostname()
PORT = 5556
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP_ADDRESS, PORT))
sock.listen(5)  # Maximum listen to 5 count
print("Server start at {}:{}".format(IP_ADDRESS, PORT))

while True:
    conn, adr = sock.accept()
    print("Connection to {} established.".format(adr))
    conn.send(bytes("Socket Programming in Python", "utf-8"))
    conn.close()
