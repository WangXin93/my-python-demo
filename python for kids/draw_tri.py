from tkinter import*
import random
tk = Tk()
canvas = Canvas(tk,width = 400,height = 400)
canvas.pack()
tri_color = ['green','red','blue','orange','yellow','pink','purple','violet',
         'magenta','cyan']
def draw_tri(size):
    a1x = random.randint(0,size)
    a1y = random.randint(0,size)
    a2x = a1x + random.randint(-size/2,size/2)
    a2y = a1y + random.randint(-size/2,size/2)
    a3x = a1x + random.randint(-size/2,size/2)
    a3y = a1y + random.randint(-size/2,size/2)
    canvas.create_polygon(a1x,a1y,a2x,a2y,a3x,a3y,
                          fill = random.choice(tri_color))
for i in range(0,100):
    draw_tri(400)
