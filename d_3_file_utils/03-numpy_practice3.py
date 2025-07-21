import numpy as np
import matplotlib.pyplot as plt
import cv2

#numpy切片在图像上的用法 并修改颜色
img = cv2.imread(r"E:\files\hibara.jpg")
img[0:100,0:100] = [0,0,255]
plt.imshow(img)
plt.show()