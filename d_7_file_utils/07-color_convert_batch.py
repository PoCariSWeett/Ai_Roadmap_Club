import os
import glob
import cv2
import matplotlib.pyplot as plt


def is_image_file(parh,exts = ['.jpg','.png']):
    _, ext = os.path.splitext(parh)
    return ext.lower() in exts

def convert_color(img,mode = 'gray'):
    if mode == 'gray':
        return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    elif mode == 'rgb':
        return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    elif mode == 'hsv':
        return cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    else:
        raise ValueError(f"不支持的转换模式: {mode}")

def save_img(img,path):
    yes = cv2.imwrite(path, img)
    if not(yes):
        print(f"保存失败{path}")
    return yes

def show_img(img, title = '图像'):
    if img is None:
        print("图像为空,无法显示")
        return
    plt.title(title)
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

def batch_color(folder_in,folder_out,mode = 'gray',preview = 3):
    os.makedirs(folder_out,exist_ok=True)
    files = glob.glob(os.path.join(folder_in,'*'))
    count_yes = 0
    count_no = 0
    preview_count = 0

    for file in files:
        if not is_image_file(file):
            continue
        img = cv2.imread(file)
        if img is None:
            print("读取失败:{file}")
            count_no += 1
            continue
        try:
            converted = convert_color(img,mode = mode)
        except Exception as e:
            print("转换失败:",e)
            count_no += 1
            continue

        name,ext = os.path.splitext(os.path.basename(file))
        suffix = f'{mode}{ext}'
        out_path = os.path.join(folder_out,name + suffix)
        if save_img(converted,out_path):
            count_yes += 1
            if preview_count < preview:
                show_img(converted,title=f"{name}_{mode}")
                preview_count += 1
        else:
            count_no += 1
    print(f"\n处理完成:成功{count_yes}张,失败{count_no}张\n")

if __name__ == '__main__':
    folder_in = input("输入原图文件夹路径: ").strip().strip('"').strip("'")
    folder_out = input("输出图像保存文件夹: ").strip().strip('"').strip("'")
    mode = input("选择颜色模式(gray|rgb|hsv): ").strip().lower()
    batch_color(folder_in,folder_out,mode = mode)