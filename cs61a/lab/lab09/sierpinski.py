from turtle import *
def tri(fn):
    for _ in range(3):
        fn()
        lt(120)

def sier(d, k):
    def to_tri():
        if k == 1:
            fd(d)
        else:
            leg(d, k)
    tri(to_tri)

def leg(d, k):
    sier(d / 2, k - 1)
    penup()
    fd(d)
    pendown()

sier(200, 4)
done()
