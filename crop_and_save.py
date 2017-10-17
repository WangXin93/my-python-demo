import os
import PIL.Image
import random

def crop_and_save(filename, savename):
	'''
	randomly crop a piece of 180x180 size from image
	Args:
		filaname: A name of image file
	Returns:
		pass
	'''
	img = PIL.Image.open(filename)
	size = img.size
	x, y = random.randint(0, size[0]-180), random.randint(0, size[1]-180)
	cropped = img.crop((x, y, x+180, y+180)).save(savename)

# 循环遍历一个目录下所有文件
 l = []
for root, dirs, files in os.walk('.'):
     for name in files:
         if str(name).endswith('.tif'):
             l.append(os.path.join(root, name))

# 为每张图片生成两张180x180的裁剪子图
for x in l:
	print(x)
	dirname = os.path.basename(x).strip('.tif')
	if not os.path.exists(os.path.join('./test', dirname)):
		os.makedirs(os.path.join('./test', dirname))
	already_have = len(os.listdir(os.path.join('./test',dirname)))
	name1 = os.path.join('./test',dirname,dirname+'-000'+str(already_have+1)+'.jpg') 
	name2 = os.path.join('./test',dirname,dirname+'-000'+str(already_have+2)+'.jpg')
	crop_and_save(x, name1)
	crop_and_save(x, name2)

