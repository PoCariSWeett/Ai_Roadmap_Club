import cv2
import matplotlib.pyplot as plt

img_path = r'E:\files\hibara.jpg'
img = cv2.imread(img_path,1) # 1=彩色
if img is None:
    print('error')
    exit()

print("origin_size: ",img.shape)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title('original')
plt.axis('off')
plt.show()

cv2.imwrite(r'E:\files\hibara.jpg',img)
print("save: hibara_copy.jpg")

small = cv2.resize(img,(64,64),interpolation=cv2.INTER_AREA)
print("resize(H,W,C): ",small.shape)

plt.imshow(cv2.cvtColor(small,cv2.COLOR_BGR2RGB))
plt.title('resize 64×64')
plt.axis('off')
plt.show()

cv2.imwrite(r'E:\files\hibara_128.jpg',small)
print("save: hibara_64.jpg")

bigger = cv2.resize(img,None,fx = 3,fy = 3,interpolation = cv2.INTER_LINEAR)
print("resize(H,W,C): ",bigger.shape)

plt.imshow(cv2.cvtColor(bigger,cv2.COLOR_BGR2RGB))
plt.title("magnify 3 times")
plt.axis('off')
plt.show()

cv2.imwrite(r'E:\files\hibara_1.5x.jpg',bigger)
print("save: hibara_1.5x.jpg")
