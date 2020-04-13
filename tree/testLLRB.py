from LLRB import LLRB, RED, BLACK
from string import ascii_lowercase
import pytest

def testInit():
    t = LLRB()
    assert t.contains(1) == False

def testDeleteMax():
    """ https://www.cs.princeton.edu/~rs/talks/LLRB/RedBlack.pdf
    Page 59
    """
    t = LLRB()
    for a in "abcdefghijklmno":
        t.put(a)
    t.deleteMaxRoot()
    t.display()
    t.deleteMaxRoot()
    t.display()

def testDeleteMin():
    t = LLRB()
    for a in "abcdefghijklmno":
        t.put(a)
    t.deleteMinRoot()
    t.display()
    t.deleteMinRoot()
    t.display()

def testDelete():
    t = LLRB()
    for i in range(10):
        t.put(i)
    t.delete(4)
    t.delete(5)
    print(t.size)
    t.display()

if __name__ == "__main__":
    testDeleteMax()
