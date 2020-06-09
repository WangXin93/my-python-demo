import socket
import select
import threading
import asyncio

IP_ADDRESS = socket.gethostname()
HEADER_LENGTH = 10
PORT = 5556


class Server:
    def __init__(self, ip_addr, port):
        self.ip_addr = ip_addr
        self.port = port
        self.writers = []

    async def start(self):
        a_server = await asyncio.start_server(
            self.handle, self.ip_addr, self.port)
        print("Sever start on {}:{}".format(self.ip_addr, self.port))
        async with a_server:
            await a_server.serve_forever()

    async def handle(self, reader, writer):
        self.writers.append(writer)
        self.send_message(writer, "Welcom to this chatroom!")
        addr = writer.get_extra_info("peername")
        message = f"{addr!r} is connected !!!"
        print(message)

        while True:
            message_header = await reader.read(HEADER_LENGTH)
            if len(message_header):
                message_length = int(message_header.decode().strip())
                message_data = await reader.read(message_length)
                message_data = message_data.decode().strip()
                print("<{}>: {}".format(addr[0], message_data))
                await self.broadcast(message_data, writer)

        writer.close()
        self.remove(writer)

    def send_message(self, conn, message):
        try:
            conn.write(message.encode())
        except BaseException:
            conn.close()
            """ If the link is broken, we remove the client"""
            self.remove(conn)

    """ using the below function, we boradcast the message to all clients
    who's object is not the same as the one sending the message"""

    async def broadcast(self, message, writer):
        for w in self.writers:
            if w != writer:
                self.send_message(w, message)
                await w.drain()

    def remove(self, connection):
        if connection in self.writers:
            print("Lost " + str(connection))
            self.writers.remove(connection)


if __name__ == "__main__":
    server = Server(IP_ADDRESS, PORT)
    asyncio.run(server.start())
