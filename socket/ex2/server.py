import pickle
import socket

HEAD = 10 # The head of message representing the length
IP_ADDRESS = socket.gethostname()
PORT = 5556
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP_ADDRESS, PORT))
sock.listen(5)
print("Server start at: {}:{}".format(IP_ADDRESS, PORT))

while True:
    conn, adr = sock.accept()
    print("Connection to {} establised".format(adr))

    m = {1: "Client", 2: "Server"}
    msg = pickle.dumps(m)
    msg = bytes(f"{len(msg):<{HEAD}}", "utf-8") + msg
    conn.send(msg)
    # You will find the client
    # conn.close()
