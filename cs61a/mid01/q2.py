def bar(f):
    def g(x):
        return f(x - 1)
    return g
f = 4
print(bar(lambda x: x + f)(2))
