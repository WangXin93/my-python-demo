import os
import sys
import pygame as pg
import socket
import threading
from textbox import TextBox


KEY_REPEAT_SETTING = (200,70)
HEADER_LENGTH = 10
IP_ADDRESS = socket.gethostname()
PORT = 5556


class Control(object):
    def __init__(self):
        pg.init()
        pg.display.set_caption("Online Chat Yeah!!!")
        self.screen = pg.display.set_mode((500,500))
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.input = TextBox((100,400,300,30),command=self.enter_message,
                              clear_on_enter=True,inactive_on_enter=False)
        self.color = (100,100,100)
        self.prompt = self.make_prompt()
        pg.key.set_repeat(*KEY_REPEAT_SETTING)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((IP_ADDRESS, PORT))

        self.messages = []

    def make_prompt(self):
        font = pg.font.SysFont("arial", 20)
        message = 'Please type you message here:'
        rend = font.render(message, True, pg.Color("white"))
        return (rend, rend.get_rect(topleft=(10,35)))

    def make_messages(self):
        font = pg.font.SysFont("arial", 20)
        out = []
        y = 65
        for message in self.messages:
            rend = font.render(message, True, pg.Color("white"))
            out.append((rend, rend.get_rect(topleft=(10,y))))
            y += 30
        return out

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.input.get_event(event)

    def update_messages(self, message):
        while len(self.messages) > 10:
            self.messages.pop(0)
        self.messages.append(message)

    def enter_message(self,id,message):
        self.update_messages("<You>: {}".format(message))
        self.send_message(message)

    def send_message(self, message):
        try:
            message_header = f"{len(message):<{HEADER_LENGTH}}"
            self.server.send(message_header.encode() + message.encode())
        except ValueError:
            print("Please input a valid message.")

    def receive_message(self):
        while True:
            try:
                message = self.server.recv(2048)
                if message:
                    message = message.decode()
                    self.update_messages(message)
            except:
                print("Closing", self.server)
                self.server.close()

    def start_network_thread(self):
        t = threading.Thread(target=self.receive_message)
        t.setDaemon(True)
        t.start()

    def main_loop(self):
        self.start_network_thread()
        while not self.done:
            self.event_loop()
            self.input.update()
            self.screen.fill(self.color)
            self.input.draw(self.screen)
            self.screen.blit(*self.prompt)
            for msg in self.make_messages():
                self.screen.blit(*msg)
            pg.display.update()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    app = Control()
    app.main_loop()
    pg.quit()
    sys.exit()
