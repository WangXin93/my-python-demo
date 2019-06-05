## Usage

```
python tryit.py
python panorama.py
```

## Harris Corner Detection

算法步骤：

1. 求出$$I(x, y)$$在x，y方向上的梯度$$Ix, Iy$$
2. 计算structure matrix的各个元素$$I_{xx} = I_x * I_x$$， $$I_{yy} = I_y * I_y$$，  $$I_{xy} = I_x * I_y$$
3. 对上面的三个元素进行高斯加权滤波
4. 求出每个像素的响应值，令小于阈值的的点（比如小于0.01*np.max(R)）的值为0
5. 进行非极大值抑制，即对于每一个点，如果它的周围邻居存在比它大的值，将它设置为0
6. 将大于阈值的点在原图像中标注出来

### Reference

* https://blog.csdn.net/lql0716/article/details/52628959
* <https://blog.csdn.net/tanhongguang1/article/details/8898927>
* <https://stackoverflow.com/questions/43525409/harris-corner-detector-python>
* <http://www.kaij.org/blog/?p=89>
* <https://muthu.co/harris-corner-detector-implementation-in-python/>
* <https://www.meccanismocomplesso.org/opencv-python-harris-corner-detection-un-metodo-per-rilevare-i-vertici-in-unimmagine/>
* https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html



## Panorama

步骤：

1. 从两个图片中寻找特征点（DoG，Harris等），对特征点提取局部不变特征（SIFT，SURF等）。
2. 将两个图片中的特征点进行匹配（Brute force，FLANN等）。
3. 使用[RANSAC算法](https://en.wikipedia.org/wiki/RANSAC)来，根据匹配的特征点来计算[homography矩阵](https://en.wikipedia.org/wiki/Homography_(computer_vision))。
4. 根据第3步得到的homography矩阵对图片进行transformation。



### Reference

* https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html
* https://www.tuicool.com/articles/RFNjaub



## RANSAC

步骤：

1. 随机从所有点中采样部分样本
2. 根据采样的样本计算得到一个homography
3. 计算该homography的变形下inliners的数量
4. 回到第1步，知道找到满足最多inliners的homography，并根据所有inliners计算出一个homography作为结果返回。



## 求解[Homography](https://en.wikipedia.org/wiki/Homography_(computer_vision))

Homography是一个$$ 3 \times3 $$ 矩阵：
$$
H = \left[\begin{matrix}
h_{00} & h_{01} & h_{02} \\
h_{10} & h_{11} & h_{12} \\
h_{20} & h_{21} & h_{22}
\end{matrix}\right]
$$
它可以用来描述两张图片之间的映射关系：
$$
\left[\begin{matrix}
x_1 \\ y_1 \\ 1
\end{matrix}\right] = 
\left[\begin{matrix}h_{00} & h_{01} & h_{02} \\h_{10} & h_{11} & h_{12} \\h_{20} & h_{21} & h_{22}\end{matrix}\right]
\left[\begin{matrix}
x_2 \\ y_2 \\ 1
\end{matrix}\right]
$$

在齐次坐标中，由于$$h_{22}$$值和第3个坐标值为1。如果需要计算projection，那么一共有8个自由度，计算一个homography最少要4个标定点。
$$
x' = (h_{00}x_2 + h_{01}y_2 + h_{02}) / (h_{20}x_2 + h_{21}y_2 + 1) \\
y' = (h_{10}x_2 + h_{11}y_2 + h_{12}) / (h_{20}x_2 + h_{21}y_2 + 1)
$$
上面的式子可以改写成方程组 $$Ma = b$$：
$$
\left[\begin{matrix}
x_2 & y_2 & 1 & 0 & 0 & 0 & -x'x_2 & -x'y_2 \\
0  & 0 & 0 & x_2 & y_2 & 1 & -y'x_2 & -y'y_2
\end{matrix}\right]
\left[\begin{matrix}
h_{00} \\ h_{01} \\ h_{02} \\ h_{10} \\ h_{11} \\ h_{12} \\ h_{20} \\ h_{21}
\end{matrix}\right] = 
\left[\begin{matrix}
x' \\ y'
\end{matrix}\right]
$$


对于超定情况可以用最小二乘求近似解。
$$
M^TM a = M^T b \\
a = (M^T M)^{-1}M^T b
$$

### Reference

* <https://cseweb.ucsd.edu/classes/wi07/cse252a/homography_estimation/homography_estimation.pdf>
* https://www.bilibili.com/video/av43498478/?p=7
