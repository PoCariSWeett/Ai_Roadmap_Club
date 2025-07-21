import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r"E:\files\hibara.jpg")

#用加减法处理像素
img = img + 50 #调亮
plt.imshow(img)
plt.show()

#反转颜色
img = 255 - img
np.clip(img,0,255,out=img)
plt.imshow(img)
plt.show()