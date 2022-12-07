'''
Author: mousechannel mochenghh@gmail.com
Date: 2022-12-06 12:07:51
LastEditors: mousechannel mochenghh@gmail.com
LastEditTime: 2022-12-07 19:24:35
FilePath: \数字图像处理2\code\dft\dft.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2 as cv

import numpy as np
import matplotlib.pyplot as plt

image_path = '../sushi.jpg'


def work1():
    img = cv.imread(image_path, 0)
    dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * \
        np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()


def work2():

    img = cv.imread(image_path, 0)
    dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    rows, cols = img.shape
    crow, ccol = rows//2, cols//2
    # 首先创建一个掩码，中心正方形为1，其余全为零,代表低通滤波
    mask = np.zeros((rows, cols, 2), np.uint8)
    offset = 60
    mask[crow-offset:crow+offset, ccol-offset:ccol+offset] = 1
    # 应用掩码和逆DFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv.idft(f_ishift)
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img_back, cmap='gray')
    plt.title('filter low_more'), plt.xticks([]), plt.yticks([])
    plt.show()


def work3():

    img = cv.imread(image_path, 0)
    dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    rows, cols = img.shape
    crow, ccol = rows//2, cols//2
    # 首先创建一个掩码，中心正方形为1，其余全为零
    mask = np.ones((rows, cols, 2), np.uint8)
    offset = 60
    mask[crow-offset:crow+offset, ccol-offset:ccol+offset] = 0
    # 应用掩码和逆DFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv.idft(f_ishift)
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img_back, cmap='gray')
    plt.title('filter high_more '), plt.xticks([]), plt.yticks([])
    plt.show()
    cv.split()


# work1()
# work2()
# work3()
