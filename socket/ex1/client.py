import socket

# IP_ADDRESS = "127.0.0.1"
IP_ADDRESS = socket.gethostname()
PORT = 5556
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP_ADDRESS, PORT))

complete_info = ""
while True:
    msg = sock.recv(7)
    if len(msg) == 0:
        break
    complete_info += msg.decode("utf-8")
print(complete_info)
