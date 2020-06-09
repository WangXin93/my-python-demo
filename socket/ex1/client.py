""" The client side socket
"""
import socket

# Some contants, skip them and read it later
# IP_ADDRESS = "127.0.0.1"
IP_ADDRESS = socket.gethostname()
PORT = 5556

# Create socket with IP address and port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP_ADDRESS, PORT))

# Use while loop to keep receive message from server
complete_info = ""
while True:
    # Receive data from server, buffer size 1
    # It means each step only receive one byte
    msg = sock.recv(1)
    if len(msg) == 0:
        break
    complete_info += msg.decode("utf-8")
    print(complete_info)
print(complete_info)
