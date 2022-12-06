'''
Author: mousechannel mochenghh@gmail.com
Date: 2022-12-06 13:37:20
LastEditors: mousechannel mochenghh@gmail.com
LastEditTime: 2022-12-06 19:54:50
FilePath: \数字图像处理2\code\dft\dct.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2  

import numpy as np
import matplotlib.pyplot as plt

# 整张图 DCT 变换
def whole_img_dct(img_f32):
    img_dct = cv2.dct(img_f32)            # 进行离散余弦变换
    img_dct_log = np.log(abs(img_dct))    # 进行log处理
    img_idct = cv2.idct(img_dct)          # 进行离散余弦反变换
    return img_dct_log, img_idct

# 分块图 DCT 变换
def block_img_dct(img_f32,size):
    
    height,width = img_f32.shape[:2]
    block_y = height // size
    block_x = width // size
    height_ = block_y * size
    width_ = block_x * size
    img_f32_cut = img_f32[:height_, :width_]
    img_dct = np.zeros((height_, width_), dtype=np.float32)
    new_img = img_dct.copy()
    for h in range(block_y):
        for w in range(block_x):
            # 对图像块进行dct变换
            img_block = img_f32_cut[size*h: size*(h+1), size*w: size*(w+1)]
            img_dct[size*h: size*(h+1), size*w: size*(w+1)] = cv2.dct(img_block)
            # 进行 idct 反变换
            dct_block = img_dct[size*h: size*(h+1), size*w: size*(w+1)]
            img_block = cv2.idct(dct_block)
            new_img[size*h: size*(h+1), size*w: size*(w+1)] = img_block
    img_dct_log2 = np.log(abs(img_dct))
    return img_dct_log2, new_img


def work():
    img_u8 = cv2.imread('../sushi.jpg', 0)
    img_f32 = img_u8.astype(np.float)  # 数据类型转换 转换为浮点型
    img_dct_log, img_idct = whole_img_dct(img_f32)
    img_dct_log2, new_img = block_img_dct(img_f32.copy(),8)
    img_dct_log3, new_img1 = block_img_dct(img_f32.copy(),16)

    # plt.figure(6, figsize=(12, 8))
    plt.subplot(131)
    plt.imshow(img_u8, 'gray')
    plt.title('original image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132)
    plt.imshow(img_dct_log)
    plt.title('DCT'), plt.xticks([]), plt.yticks([])
    plt.subplot(133)
    plt.imshow(img_idct, 'gray')
    plt.title('IDCT'), plt.xticks([]), plt.yticks([])
    
    plt.show()
    
    plt.subplot(131)
    plt.imshow(img_u8, 'gray')
    plt.title('original image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132)
    plt.imshow(img_dct_log2)
    plt.title('block_DCT_8'), plt.xticks([]), plt.yticks([])
    plt.subplot(133)
    plt.imshow(new_img, 'gray')
    plt.title('block_IDCT_8'), plt.xticks([]), plt.yticks([])
    
    plt.show()
    
    plt.subplot(131)
    plt.imshow(img_u8, 'gray')
    plt.title('original image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132)
    plt.imshow(img_dct_log3)
    plt.title('block_DCT_16'), plt.xticks([]), plt.yticks([])
    plt.subplot(133)
    plt.imshow(new_img1, 'gray')
    plt.title('block_IDCT_16'), plt.xticks([]), plt.yticks([])
    plt.show()
    
work()