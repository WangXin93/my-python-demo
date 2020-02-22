import socket
import pickle

a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2000))

while True:
    complete_info = b""
    rev_msg = True
    while True:
        msg = s.recv(16)
        if rev_msg:
            print(f"The length of message = {msg[:a]}")
            x = int(msg[:a])
            rev_msg = False
        complete_info += msg
        if len(complete_info) - a == x:
            print("Recieved the complete info")
            print(complete_info[a:])
            m = pickle.loads(complete_info[a:])
            print(m)
            rev_msg = True
            complete_info = b""
    print(complete_info)
