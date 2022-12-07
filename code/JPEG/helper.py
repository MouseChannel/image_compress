'''
Author: mousechannel mochenghh@gmail.com
Date: 2022-12-07 19:24:21
LastEditors: mousechannel mochenghh@gmail.com
LastEditTime: 2022-12-07 19:49:57
FilePath: \数字图像处理2\code\JPEG\helper.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2 as cv
import numpy as np

def RMSE(data, origin):
    size = data.size
    sum = 0
    n = data.shape[0]
    m = data.shape[1]
    for i in range(n):
        for j in range(m):
            sum = sum + np.square(int(data[i][j]) -  origin[i][j] )
    sum = sum / size
    return np.sqrt(sum)

img1 = cv.imread('./noddles.png', 0)

 
    
 
img2 = cv.imread('./noddles_after_20.jpeg', 0)
img3 = cv.imread('./noddles_after_40.jpeg', 0)
img4 = cv.imread('./noddles_after_60.jpeg', 0)
print(img1.shape)
 
print('noddles_after_20 RMSE = ', RMSE(img1,img2))
 
print('noddles_after_40 RMSE = ', RMSE(img1,img3))
 
print('noddles_after_60 RMSE = ', RMSE(img1,img4))

# plt.subplot(221), plt.imshow(img1, cmap='gray')

# plt.title('Input Image size = 291K'), plt.xticks([]), plt.yticks([])
# plt.subplot(222), plt.imshow(img2, cmap='gray')
# plt.title('Quality factor=20 size = 238K'), plt.xticks([]), plt.yticks([])
# plt.subplot(223), plt.imshow(img3, cmap='gray')
# plt.title('Quality factor=40 size = 258K'), plt.xticks([]), plt.yticks([])
# plt.subplot(224), plt.imshow(img4, cmap='gray')
# plt.title('Quality factor=60 size = 268K'), plt.xticks([]), plt.yticks([])
# plt.show()
