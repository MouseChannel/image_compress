'''
Author: mousechannel mochenghh@gmail.com
Date: 2022-12-06 14:50:45
LastEditors: mousechannel mochenghh@gmail.com
LastEditTime: 2022-12-06 15:01:41
FilePath: \数字图像处理2\code\RLE\rle.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
##彩色图像灰度化
#image = cv.imread('image/shayu.jpg',1)
image = cv.imread('../cartoon_1.png',1)
grayimg = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
rows, cols = grayimg.shape

image1 = grayimg.flatten() #把灰度化后的二维图像降维为一维列表
#print(len(image1))

#二值化操作
# for i in range(len(image1)):
#     if image1[i] >= 127:
#         image1[i] = 255
#     if image1[i] < 127:
#         image1[i] = 0

data = []
image3 = []
count = 1
#行程压缩编码
for i in range(len(image1)-1):
    if (count == 1):
        image3.append(image1[i])
    if image1[i] == image1[i+1]:
        count = count + 1
        if i == len(image1) - 2:
            image3.append(image1[i])
            data.append(count)
    else:
        data.append(count)
        count = 1

if(image1[len(image1)-1] != image1[-1]):
    image3.append(image1[len(image1)-1])
    data.append(1)

#压缩率
ys_rate = len(image3)/len(image1)*100
print('压缩率为' + str(ys_rate) + '%')

#行程编码解码
rec_image = []
for i in range(len(data)):
    for j in range(data[i]):
        rec_image.append(image3[i])

rec_image = np.reshape(rec_image,(rows,cols))

# cv.imwrite('./output.png',rec_image)
# cv.imwrite('image/output_fruit.jpg',rec_image)
plt.subplot(121),plt.imshow(grayimg, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(rec_image, cmap = 'gray')
plt.title('after'), plt.xticks([]), plt.yticks([])
plt.show()
# cv.waitKey(0) 
#  压缩率为44.258676520140035%
# 压缩率为24.172453703703702%