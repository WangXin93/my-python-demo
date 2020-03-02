class Email:
    """Every email object has 3 instance attributes: the message, the sender name,
    and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Mailman:
    """Each Mailman has an instance attribute clients, which is a dictionary that
    associates client names with client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the box of the client it is addressed to."""
        if email.recipient_name not in self.clients.keys():
            print("Not registered: " + email.recipient_name)
        else:
            self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it to the clients instance
        attributes."""
        if client_name in self.clients.keys():
            print("Already registered: " + client_name)
        else:
            self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is used for addressing emails
    to the client), mailman(which is used to send emails out to other clients), and
    inbox(a list of all emails the client has received)
    """
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name
        self.mailman.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""
        mail = Email(msg, self.name, recipient_name)
        self.mailman.send(mail)
    
    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        self.inbox.append(email)

qiubite = Mailman()
azhen = Client(qiubite, 'azhen')
aqiang = Client(qiubite, 'aqiang')
azhen.compose('I love you, qiang', 'aqiang')