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
img1 = cv.imread('../cartoon_1.png', 0)
 
img2 = cv.imread('../cartoon_1_after_20.jpeg', 0)
img3 = cv.imread('../cartoon_1_after_40.jpeg', 0)
img4 = cv.imread('../cartoon_1_after_60.jpeg', 0)
 
plt.subplot(221), plt.imshow(img1, cmap='gray')

plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(img2, cmap='gray')
plt.title('Quality factor=20'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(img3, cmap='gray')
plt.title('Quality factor=40'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img4, cmap='gray')
plt.title('Quality factor=60'), plt.xticks([]), plt.yticks([])
plt.show()
