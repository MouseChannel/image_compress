'''
Author: mousechannel mochenghh@gmail.com
Date: 2022-12-06 15:22:11
LastEditors: mousechannel mochenghh@gmail.com
LastEditTime: 2022-12-06 15:32:04
FilePath: \数字图像处理2\code\JPEG\Test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import RGB2YUV
import DCT
import Quantization
import AC
import DC
import Compress
import cv2

def printBlock(block):
    for row in block:
        print(row)


img = cv2.imread('../cartoon_1.png')
DCT = DCT.DCT()
Quantization = Quantization.Quantization()
AC = AC.AC()
DC = DC.DC()
Compress = Compress.Compress()
Y, U, V = RGB2YUV.rgb2yuv(img, img.shape[1], img.shape[0])
Y = DCT.fill(Y)
blocks = DCT.split(Y)
first = blocks[0]
print('The first block of Y:')
printBlock(first)
print('')
print('The DCT of the block:')
first = DCT.FDCT(first)
printBlock(first)
print('')
print('The Quantization of the DCT:')
first = Quantization.quanY(first)
printBlock(first)
print('')
Z = AC.ZScan(first)
DC = first[0][0]
AC = AC.RLC(Z)
print('Z : ' + str(Z))
print('DC: ' + str(DC))
print('AC: ' + str(AC))
print('AClen: ' + str(len(AC)))
Bstr = Compress.AllCompressY(DC, AC)
print(Bstr)
print(len(Bstr))




