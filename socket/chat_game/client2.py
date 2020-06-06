import socket
import selectors
import sys

IP_ADDRESS = socket.gethostname()
PORT = 5556
HEADER_LENGTH = 10
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP_ADDRESS, PORT))

sel = selectors.DefaultSelector()

def read_sock(conn, mask):
    message = conn.recv(2048)
    if message:
        print(message.decode())
    else:
        print("Closing", conn)
        sel.unregister(conn)
        conn.close()

def read_stdin(conn, mask):
    message = conn.readline()
    message_header = f"{len(message):<{HEADER_LENGTH}}"
    server.send(message_header.encode() + message.encode())
    sys.stdout.write("<You>")
    sys.stdout.write(message)
    sys.stdout.flush()

sel.register(server, selectors.EVENT_READ, read_sock)
sel.register(sys.stdin, selectors.EVENT_READ, read_stdin)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
