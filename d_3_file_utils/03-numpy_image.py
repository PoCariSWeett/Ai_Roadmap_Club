import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"E:\files\hibara.jpg")

if img is None:
    print("读取失败")
    exit()

print("img_shape",img.shape)
print("img_dtype",img.dtype)
print("first_element",img[0,0])

#显示原图
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("original_picture")
plt.show()
plt.axis('off')
plt.show()