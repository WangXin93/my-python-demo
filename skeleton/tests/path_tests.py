from nose.tools import *
from mkskl import *
import shutil

def setup_test():
    print("SETUP!")

def touch_test():
    # Can't suppurt '.', ''
    path = './d1/f1'
    touch(path)
    assert_true(os.path.exists(path))
    os.system("rm -rf d1") 
    
    path = 'a1'
    touch(path)
    assert_true(os.path.exists(path))
    os.system("rm a1")

