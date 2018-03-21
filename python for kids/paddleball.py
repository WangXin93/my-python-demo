from tkinter import*
import random
import time

class Ball:
    def __init__(self,canvas,color,paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.gameOver = canvas.create_text(250,200,text = 'game over!',
                                           font = ('Courier',20),
                                           state = 'hidden')
        self.score = 0
        self.scoreShow = canvas.create_text(50,10,text = 'score:%s'%self.score,
                                            font = ('Courier',10),
                                            fill = 'green')
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.isMoving = False
        self.canvas.bind_all('<KeyPress-Up>',self.change_state)

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def change_state(self,evt):
        self.isMoving = not self.isMoving
        
    def draw(self):
        if self.isMoving == True:
            self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            time.sleep(0.5)
            self.canvas.itemconfig(self.gameOver,state = 'normal')
        if pos[0] <= 0:
            self.x = 3
        if pos[1] <= 0:
            self.y = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.score = self.score + 1
            self.canvas.itemconfig(self.scoreShow,text = 'score:%s'%self.score)
            self.x = self.paddle.x + self.x
            self.y = -3
            
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill = color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left(self,evt):
        self.x = -2
    def turn_right(self,evt):
        self.x = 2

tk = Tk()
tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk,width = 500,height = 400,bd = 0,highlightthickness = 0)
canvas.pack()
tk.update()

paddle = Paddle(canvas,'blue')
ball = Ball(canvas,'red', paddle)

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
