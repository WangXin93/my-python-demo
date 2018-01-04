import shutil
import os

names = []
f = open('test.txt', 'r')
names = f.readlines()
for name in names:
	src = 'images/' + name.strip('\n') + '.jpg'
	dst = os.path.basename(name)
	dst = 'test/' + dst.strip('\n') + '.jpg'
	dirname = os.path.dirname(dst)
	shutil.copy(src, dst)
