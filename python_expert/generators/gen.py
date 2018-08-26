# gen.py

# top-level syntax, function --> underscore method
# x()     -->       __call__

from time import sleep

def compute():
    pass

class Compute:
    def __call__(self):
        rv = []
        for i in range(100):
            sleep(0.5)
            rv.append(i)
        return rv
    def __iter__(self):
        self.last = 0
        return self
    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv

def compute():
    for i in range(10):
        sleep(.5)
        yield i

compute = Compute()

# __iter__
# for x in xs:
#     pass

# iterator has __next__
# x = iter(x)
# while True:
#     next(x)

def Api:
    def run_this_first(self):
        first()
    def run_this_second(self):
        second()
    def run_this_last(self):
        last()

Api().run_this_last()
Api().run_this_second()
Api().run_this_first()

# Guaratee the sequence order
def api():
    first()
    yield
    second()
    yield
    last()

# When you are on the library side, you should make sure user can use it correctly.
