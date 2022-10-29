import cv2
import numpy as np

output_dir = r"D:\1. 研究生\项目\MMA-Net\dataset\output\VIL100\60_lr0.001deay1e-6_sgd"
dataset_dir = r"D:\1. 研究生\项目\MMA-Net\dataset\VIL100"

img1 = cv2.imread('00000.jpg')
img2 = cv2.imread('output-00000.png')

imgadd = cv2.add(img1, img2)
cv2.imshow('imgadd', imgadd)
cv2.imwrite('output.jpg', imgadd)
cv2.waitKey(0)