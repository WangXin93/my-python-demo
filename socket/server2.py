import pickle
import socket

a = 10 # The head of message representing the length
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2000))
s.listen(5)

while True:
    clt, adr = s.accept()
    print("Connection to {} establised".format(adr))

    m = {1: "Client", 2: "Server"}
    msg = pickle.dumps(m)
    msg = bytes(f"{len(msg):<{a}}", "utf-8") + msg
    clt.send(msg)
