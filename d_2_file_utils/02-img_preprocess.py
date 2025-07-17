import os
import cv2
import matplotlib.pyplot as plt

#用cv2.imread读取图像,支持中文路径的话要做特殊处理
def read_img(img_path):
    #更正:增加读取图像失败的处理
    img = cv2.imread(img_path)
    if img is None:
        print(f'读取失败:{img_path}')
    return img

#图像转灰度
def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def resize_img(img,size = (256,256)):
    return cv2.resize(img,size)

def show_img(img,title = 'img'):
    plt.title(title)
    if img is None:
        plt.text(0.5,0.5,"图像为空", ha='center')
    else:
        if len(img.shape) == 2:
            plt.imshow(img, cmap='gray')
        else:
            plt.imshow(img,cmap='gray')
    plt.axis('off')
    plt.show()
def save_img(img,save_path):
    yes = cv2.imwrite(save_path,img)
    if not(yes):
        print(f"保存失败:{save_path}")
    return yes

if __name__ == '__main__':

    path = input("输入图片路径: ")

    img = read_img(path)
    if img is not None:
        gray = to_gray(img)
        small = resize_img(gray,(128,128))
        show_img(small,'gray')
        save_img(small,"output_small_gray.jpg")
        print("保存完成: output_small_gray.jpg")
