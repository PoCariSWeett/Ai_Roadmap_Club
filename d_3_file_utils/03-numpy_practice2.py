import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"E:\files\hibara.jpg")

img[50,50] = [0,0,255]
plt.imshow(img)
plt.show()