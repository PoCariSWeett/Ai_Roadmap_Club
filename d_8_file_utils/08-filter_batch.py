import os
import cv2
import glob
import matplotlib.pyplot as plt

def is_image_file(path, exts=('.jpg', '.jpeg', '.png')):
    _, ext = os.path.splitext(path)
    return ext.lower() in exts

def show_img(img, title='图像'):
    plt.title(title)
    if img is None:
        print("图像为空，无法显示")
        return
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# 选择滤波方式并应用
def apply_filter(img, mode='blur', ksize=5):
    if mode == 'blur':
        return cv2.blur(img, (ksize, ksize))
    elif mode == 'gaussian':
        return cv2.GaussianBlur(img, (ksize, ksize), 0)
    elif mode == 'median':
        return cv2.medianBlur(img, ksize)
    else:
        raise ValueError(f"不支持的滤波模式: {mode}")

# 批量滤波函数
def batch_filter(folder_in, folder_out, mode='blur', ksize=5, preview=3):
    os.makedirs(folder_out, exist_ok=True)
    files = glob.glob(os.path.join(folder_in, '*'))
    count_yes = 0
    count_no = 0
    preview_count = 0

    for file in files:
        if not is_image_file(file):
            continue
        img = cv2.imread(file)
        if img is None:
            print(f"读取失败: {file}")
            count_no += 1
            continue

        try:
            filtered = apply_filter(img, mode=mode, ksize=ksize)
        except Exception as e:
            print(f"滤波失败: {e}")
            count_no += 1
            continue

        name, ext = os.path.splitext(os.path.basename(file))
        out_path = os.path.join(folder_out, f'{name}_{mode}{ext}')
        if cv2.imwrite(out_path, filtered):
            count_yes += 1
            if preview_count < preview:
                show_img(filtered, f'{name}_{mode}')
                preview_count += 1
        else:
            print(f"保存失败: {out_path}")
            count_no += 1

    print(f"\n批量滤波完成：成功 {count_yes} 张，失败 {count_no} 张\n")

if __name__ == '__main__':
    folder_in = input("输入原图文件夹路径：").strip().strip('"').strip("'")
    folder_out = input("输出图像保存文件夹：").strip().strip('"').strip("'")
    mode = input("选择滤波模式 (blur | gaussian | median)：").strip().lower()
    ksize = int(input("滤波核大小 (如 3 / 5 / 7)：").strip())
    batch_filter(folder_in, folder_out, mode=mode, ksize=ksize)