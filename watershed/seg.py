# https://segmentfault.com/a/1190000015690356
# http://www.cmm.mines-paristech.fr/~beucher/wtshed.html

"""
分水岭算法简介

任何灰度图像都可以看作是地形表面，其中高强度表示山峰和丘陵，而低强度表示山谷.用不同颜色的水（标签）填充每个孤立的山谷（局部最小值），随着水的上升，明显具有不同的颜色的水将开始融合.为避免这种情况，需要在水合并的位置建立障碍，在所有的山峰都被水淹没之前，要继续填满水和建造栅栏的工作然后你创建的障碍会给你分割的结果，这就是分水岭背后的“哲学”.

这种方法会导致由于噪声或图像中任何其他不正常的情况而导致的结果过于分散, 因此，OpenCV实现了一个基于标记的分水岭算法，可以在其中指定要合并的和不合并的谷点.这是一个交互式的图像分割,我们所做的就是给我们所知道的对象提供不同的标签,用一种颜色（或强度）标记我们确定为前景或对象的区域，用另一种颜色标记我们确定为背景或非对象的区域，最后标记我们不确定的区域为0，然后应用分水岭算法，我们的标记将会随着我们所给出的标签进行更新，对象的边界将值为-1.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

fname = 'case1_1.jpg'
img = cv2.imread(fname)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Otsu 阈值化处理
ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# 闭运算，可以消除一些细小的边界，消除噪声
kernel=np.ones((3, 3),np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

# 强背景区域
sure_bg = cv2.dilate(closing, kernel)

# distanceTransform方法用于计算图像中每一个非零点距离离自己最近的零点的距离，
dist_transform = cv2.distanceTransform(closing,cv2.DIST_L2,5)
# 强前景区域
ret, sure_fg = cv2.threshold(dist_transform, 0.1*dist_transform.max(),255,0)

# 强背景区域减去强前景区域，找到未知区域
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# 用连通域作为Marker 标记
ret, markers = cv2.connectedComponents(sure_fg)
# 将位置区域标记为0，其它位置从1开始
markers = markers + 1
markers[unknown==255] = 0

# 分水岭算法
markers = cv2.watershed(img,markers)

# 将边缘区域标记为-1， 将它们的像素值设置为红色
img[markers == -1] = [255,0,0]

plt.subplot(121)
plt.imshow(markers, cmap='gray')
plt.title('Markers')
plt.axis('off')
plt.subplot(122)
plt.imshow(img)
plt.title('Edges')
plt.axis('off')
plt.show()
