import time
import functools

def timer(func):
    @functools.wraps(func)
    def _func(*a, **kw):
        since = time.time()
        out = func(*a, **kw)
        elaspe = time.time() - since
        print(func.__name__, "Elasped: ", elaspe)
        return out
    return _func

@timer
def add(x, y=10):
    return x + y

add.__code__.co_code
#b'|\x00|\x01\x17\x00S\x00'
add.__defaults__
#(10,)
add.__code__.co_nlocals
#2
add.__code__.co_varnames
#('x', 'y')
from inspect import getsource
print(getsource(add))
#def add(x, y=10):
#    return x + y
from inspect import getfile
getfile(add)
#'dec.py'
