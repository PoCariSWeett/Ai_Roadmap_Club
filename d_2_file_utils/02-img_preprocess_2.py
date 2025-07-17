import os
import glob
import cv2
import matplotlib.pyplot as plt

#增加两个工具函数
def is_image_file(path,exts=('.jpg','.jpeg','.png')):
    _, ext = os.path.splitext(path)
    return ext.lower() in exts

def batch_process(folder_in,folder_out,size=(256,256),preview = 3):
    os.makedirs(folder_out,exist_ok=True)
    exts = ('.jpg','.jpeg','.png')
    files = glob.glob(os.path.join(folder_in,'*'))
    count_yes = 0
    count_no = 0

    preview_show = 0
    for file in files:
        if not is_image_file(file,exts):
            continue
        img = read_img(file)
        if img is None:
            count_no += 1
            continue

        gray = to_gray(img)
        small = resize_img(gray,size)
        base = os.path.basename(file)
        name,ext = os.path.splitext(base)
        out_name = f'{name}_gray{ext}'
        out_path = os.path.join(folder_out,out_name)

        yes = save_img(small,out_path)
        if yes:
            count_yes += 1
        else:
            count_no += 1

        #更新: 能预览前3张
        if yes and preview_show < preview:
            show_img(small,title=f'预览{name}_128×128_gray')
            preview_show += 1
    print(f'批量完成: 成功{count_yes}张,失败{count_no}张')


#用cv2.imread读取图像,支持中文路径的话要做特殊处理
def read_img(img_path):
    '''更正:增加读取图像失败的处理'''
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
        plt.axis('off')
        if len(img.shape) == 2:
            plt.imshow(img, cmap='gray')
        else:
            plt.imshow(img,cv2.COLOR_BGR2RGB)
    plt.show()
def save_img(img,save_path):
    yes = cv2.imwrite(save_path,img)
    if not(yes):
        print(f"保存失败:{save_path}")
    return yes

#更正主入口,增加批量处理
if __name__ == '__main__':

    '''path = input("输入图片路径: ")'''
    # 更正: 保证读取图像路径的时候带引号也能正常运行
    input_path = input("输入路径(图片或者文件夹): ").strip().strip('"').strip("'")

    if os.path.isdir(input_path):
        print("批量处理...")
        batch_process(input_path,"output_batch",size=(128,128))
    elif os.path.isfile(input_path):
        img = read_img(input_path)
        if img is not None:
            gray = to_gray(img)
            small = resize_img(gray,size=(128,128))
            show_img(small,"gray")
            base = os.path.basename(input_path)
            name,ext = os.path.splitext(base)
            out_path_ = f'{name}_128×128_gray{ext}'
            save_img(small,out_path_)
            print("保存成功: ",out_path_)
        else:
            print("读取失败: ",input_path)
    else:
        print("错误,请检查路径是否正确")
