# https://scikit-image.org/docs/dev/auto_examples/transform/plot_ssim.html#sphx-glr-auto-examples-transform-plot-ssim-py
# https://blog.csdn.net/ecnu18918079120/article/details/60149864
import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float, io, color
from skimage.measure import compare_ssim as ssim

from scipy import signal
from scipy import ndimage


def mse(x, y):
    return np.linalg.norm(x - y)

def fspecial(func_name,kernel_size=3,sigma=1):
    if func_name=='gaussian':
        m=n=(kernel_size-1.)/2.
        y,x= np.ogrid[-m:m+1,-n:n+1]
        h=np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
        h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
        sumh=h.sum()
        if sumh!=0:
            h/=sumh
        return h

def my_ssim(ima, imb):
    K = [0.01, 0.03]
    L = 255
    C1 = (K[0] * L) * (K[0] * L)
    C2 = (K[1] * L) * (K[1] * L)
    w = fspecial('gaussian', 11, 1.5)

    ua = signal.convolve2d(ima, w, mode='valid')
    ub = signal.convolve2d(imb, w, mode='valid')

    ua_sq = ua * ua
    ub_sq = ub * ub
    ua_ub = ua * ub

    siga_sq = signal.convolve2d(ima*ima, w, mode='valid') - ua_sq
    sigb_sq = signal.convolve2d(imb*imb, w, mode='valid') - ub_sq
    sigab = signal.convolve2d(ima*imb, w, mode='valid') - ua_ub
    
    ssim_map = ((2*ua_ub + C1) * (2*sigab + C2)) / ((ua_sq + ub_sq + C1) * (siga_sq + sigb_sq + C2))

    mssim = ssim_map.mean()
    return mssim


if __name__ == "__main__":
    img = color.rgb2gray(io.imread('dog.jpg'))
    img = img * 255
    rows, cols = img.shape

    noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
    noise[np.random.random(size=noise.shape) > 0.5] *= -1

    img_noise = img + noise
    img_const = img + abs(noise)
    print(my_ssim(img, img_noise))
    print(my_ssim(img, img_const))