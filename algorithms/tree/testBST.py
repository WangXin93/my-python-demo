from BST import BST
import pytest

def testInit():
    t = BST()
    assert t.contains(1) == False

def testPut():
    t = BST()
    t.put(2)
    t.put(1)
    t.put(3)
    assert t.contains(1)

def testDelete():
    t = BST()
    t.put(2)
    t.put(1)
    t.put(3)
    t.delete(1)
    assert not t.contains(1)

if __name__ == "__main__":
    testPut()
