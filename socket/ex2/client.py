import socket
import pickle

IP_ADDRESS = socket.gethostname()
PORT = 5556
HEAD = 10
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP_ADDRESS, PORT))

complete_info = b""
rev_msg = True
while True:
    msg = sock.recv(16)
    if rev_msg:
        x = int(msg[:HEAD])
        print("The length of message = {}".format(x))
        rev_msg = False
    complete_info += msg
    if len(complete_info) - HEAD == x:
        print("Recieved the complete info: {}".format(complete_info[HEAD:]))
        m = pickle.loads(complete_info[HEAD:])
        print("Unpickled object: {}".format(m))
        rev_msg = True
        complete_info = b""
print(complete_info)
