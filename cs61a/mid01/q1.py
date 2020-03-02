apple=4

def orange(apple):
    apple = 5
    def plum(x):
        return lambda plum: plum * 2
    return plum

print(orange(apple)("hiii")(4))
