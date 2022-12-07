'''
Author: mousechannel mochenghh@gmail.com
Date: 2022-12-06 15:22:11
LastEditors: mousechannel mochenghh@gmail.com
LastEditTime: 2022-12-07 14:12:36
FilePath: \数字图像处理2\code\JPEG\Quantization.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import numpy as np


class Quantization:
    table_origin = np.array([
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]]
    )

    table1 = np.array([

        [17, 18, 24, 47, 99, 99, 99, 99],
        [18, 21, 26, 66, 99, 99, 99, 99],
        [24, 26, 56, 99, 99, 99, 99, 99],
        [47, 66, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99]]
    )
    # w = 40
    table0 = table_origin

    def set_W(self, w):
        if w < 50:
            self.table0 = (50 * self.table_origin) / w + 0.5
        else:
            self.table0 = (2 - w / 50) * self.table_origin + 0.5
            # for i in self.table0:
            #     for j in i:
            #         j = max(j, 1)

    def Get(self):
        return self.table0

    def quanY(self, img):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                temp[i][j] = round(img[i][j] / self.table0[i][j])
        return temp

    def quanUV(self, img):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                temp[i][j] = round(img[i][j] / self.table1[i][j])
        return temp

    def reY(self, img):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                temp[i][j] = round(img[i][j] * self.table0[i][j])
        return temp

    def reUV(self, img):
        temp = [[0 for i in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                temp[i][j] = round(img[i][j] * self.table1[i][j])
        return temp


test = Quantization()
test.set_W(60)
print(test.table0)

'''
test = Quantization()
DCT = \
    [
        [190.0, 116.0, -62.0, 70.0, -12.0, -1.0, -2.0, 1.0],
        [-63.0, -15.0, 9.0, -1.0, 1.0, 0.0, -1.0, 0.0],
        [-65.0, 8.0, 38.0, -4.0, -0.0, 1.0, 0.0, -0.0],
        [3.0, -2.0, -5.0, -1.0, -1.0, -1.0, 0.0, -0.0],
        [2.0, 2.0, 2.0, 1.0, 1.0, -2.0, 1.0, -1.0],
        [-2.0, 1.0, -3.0, 1.0, 1.0, 1.0, 1.0, -1.0],
        [-2.0, 1.0, -3.0, -2.0, -1.0, -1.0, -1.0, -1.0],
        [-0.0, 2.0, 1.0, 1.0, 0.0, -0.0, 1.0, 1.0]
    ]
output = test.quanY(DCT)
for row in output:
    print(row)
'''
