"""
* Sockets are interior endopoints built for sending and receiving data
* A single network will have two sockets
* Sockets are a combination of an IP address and a Port
"""
import socket

# Define some constants here, you can skip this paragraph and read it later
# IP_ADDRESS = "127.0.0.1"
IP_ADDRESS = socket.gethostname()
PORT = 5556

# Create a socket, a socket is a combination of IP address and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP_ADDRESS, PORT))

# This socket listen to maximum 5 clients
sock.listen(5)
print("Server start at {}:{}".format(IP_ADDRESS, PORT))

while True:
    # Client socket is accepted, named conn
    conn, addr = sock.accept()
    print("Connection to {} established.".format(addr))
    # Send string to the client, here send bytes need to be encoded
    conn.send(bytes("Socket Programming in Python", "utf-8"))
    # If server side socket close, the client side will also close
    conn.close()
