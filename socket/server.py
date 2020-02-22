"""
* Sockets are interior endopoints built for sending and receiving data
* A single network will have two sockets
* Sockets are a combination of an IP address and a Port
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1023))
s.listen(5)

while True:
    clt, adr = s.accept()
    print("Connection to {} established.".format(adr))
    clt.send(bytes("Socket Programming in Python", "utf-8"))
    clt.close()
