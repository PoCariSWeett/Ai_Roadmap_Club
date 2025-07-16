import os
import glob

def list_images(folder_path, suffix_list=['.jpg', '.png','.jpeg','.bmp']):
    try:
        all_files = glob.glob(os.path.join(folder_path, '*'))

        print(f"\n 图像文件列表(文件夹: {folder_path}):\n")

        found = False
        count = 0
        total_size = 0
        with open("output.txt", "w", encoding="utf-8") as f:
            for file_path in all_files:
                _, ext = os.path.splitext(file_path)
                if ext.lower() in suffix_list:
                    found = True
                    file_name = os.path.basename(file_path)
                    file_size = os.path.getsize(file_path)
                    print(f"{file_name}: {file_size} bytes")
                    f.write(f"{file_name}: {file_size} bytes\n")
                    count += 1
                    total_size += file_size
            if not found:
                print("没有找到符合格式的图片诶~")
    except FileNotFoundError:
        print("错误!文件夹路径不存在!!")
    except Exception as error:
        print("出错啦~", error)

    print("count = "+str(count))
    print("total_size = " + str(total_size))

if __name__ == '__main__':
    folder = input("请输入图片文件夹路径~\n")
    list_images(folder)
