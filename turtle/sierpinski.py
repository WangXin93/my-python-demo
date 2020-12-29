import turtle

t = turtle.Turtle()

limit = 32

def draw_triangle(t, step):
    t.begin_fill()
    t.forward(step)
    t.left(120)
    t.forward(step)
    t.left(120)
    t.forward(step)
    t.end_fill()
    t.left(120)

def draw_sierpinski(t, step):
    if step <= limit:
        draw_triangle(t, step)
    else:
        substep = step / 2
        draw_sierpinski(t, substep)
        t.up()
        t.forward(substep)
        t.down()
        draw_sierpinski(t, substep)
        t.left(120)
        t.forward(substep)
        t.right(120)
        draw_sierpinski(t, substep)
        t.up()
        t.right(120)
        t.forward(substep)
        t.left(120)

draw_sierpinski(t, 256)
