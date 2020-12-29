"""
https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1206/lectures/fractals/
"""
import turtle

limit = 3

def draw_snowflake_line(t, step):
    if step <= limit:
        t.forward(step)
    else:
        substep = step / 3
        draw_snowflake_line(t, substep)
        t.left(60)
        draw_snowflake_line(t, substep)
        t.right(120)
        draw_snowflake_line(t, substep)
        t.left(60)
        draw_snowflake_line(t, substep)

def draw_snowflake(t, step):
    draw_snowflake_line(t, step)
    t.right(120)
    draw_snowflake_line(t, step)
    t.right(120)
    draw_snowflake_line(t, step)

t = turtle.Turtle()
s = t.getscreen()
draw_snowflake(t, step=243)
