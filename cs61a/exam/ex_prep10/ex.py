# Q1
class FlatMapper:
    """
    >>> shutter = lambda x: [x, x]
    >>> m = FlatMapper(shutter)
    >>> g = m.flat_map((2, 3, 4, 5))
    >>> list(g)
    [2, 2, 3, 3, 4, 4, 5, 5]
    """
    def __init__(self, fn):
        self.fn = fn

    def flat_map(self, s):
        for it in map(self.fn, s):
            yield from it

# Q2
class Adele:
    times = '1000'
    def __init__(self, you):
        self.call = you
    def __str__(self):
        return self.times

class Hello(Adele):
    def __next__(self):
        return next(self.call)

never = iter('cheme2Bhome')

def any(more):
    next(never)
    print(outside)
    yield next(never)
    print(next(never))
    yield more(more)

# Q3
def amplify(f, x):
    """Yield the longest sequence x, f(x), f(f(x)), ... that are true values.

    >>> list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    """
    while x:
        yield x
        x = f(x)
