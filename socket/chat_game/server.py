"""
Reference:
* https://levelup.gitconnected.com/learn-python-by-building-a-multi-user-group-chat-gui-application-af3fa1017689
* https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
"""
import socket
import select
import threading

IP_ADDRESS = socket.gethostname()
HEADER_LENGTH = 10
PORT = 5556


class Server:
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port
        """The First argument AF_INET is the address domain of the
        socket. This is used when we have an Internet Domain with
        any two hosts. The second argument is the type of socket,
        SOCK_STREAM means that data or characters are read in a
        continuous flow."""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        """ Binds the server to an entered IP address and at the
        specified port number.
        The client must be aware of these parameters.
        """
        self.sock.bind((IP_ADDRESS, PORT))
        print("Server established: " + self.ip_addr + ":" + str(self.port))
        """ Listens for 100 active connections. This number can be increased
        as per convenience.
        """
        self.sock.listen(100)

        self.clients = []
        self.client_names = []

    def start(self):
        while True:
            """ Accepts a connection request and stores two parameters,
            conn which is a socket object for that user, and addr
            which contains the IP address of the client that just
            connected"""
            conn, addr = self.sock.accept()
            self.clients.append(conn)
            print(addr[0] + " connected")
            threading._start_new_thread(self.clientthread, (conn, addr))
        conn.close()
        self.sock.close()

    def receive_message(self, conn, addr):
        message_header = conn.recv(HEADER_LENGTH)
        if len(message_header):
            message_length = int(message_header.decode().strip())
            message_data = conn.recv(message_length).decode().strip()
            """ Prints the message and address of the user who just
            sent the message on the server terminal"""
            print("<{}>: {}".format(addr[0], message_data))
            return message_data
        else:
            return None

    def clientthread(self, conn, addr):
        conn.send(b"Welcome to this chatroom!")

        while True:
            try:
                message = self.receive_message(conn, addr)
                if message:
                    message_to_send = "<{}> {}".format(addr[0], message)
                    self.broadcast(message_to_send, conn)
                else:
                    """message may have no content if the connection is
                    broken, in this case we remove the connection"""
                    self.remove(conn)
            except BaseException:
                continue

    def send_message(self, conn, message):
        try:
            conn.send(message.encode())
        except BaseException:
            conn.close()
            """ If the link is broken, we remove the client"""
            self.remove(conn)

    """ using the below function, we boradcast the message to all clients
    who's object is not the same as the one sending the message"""

    def broadcast(self, message, connection):
        for client in self.clients:
            if client != connection:
                self.send_message(client, message)

    def remove(self, connection):
        if connection in self.clients:
            print("Lost " + str(connection))
            self.clients.remove(connection)


if __name__ == "__main__":
    server = Server(IP_ADDRESS, PORT)
    server.start()
