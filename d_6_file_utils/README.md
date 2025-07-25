## day6📖 OpenCV读图与缩放

#### 目标🤺
- 熟悉 OpenCV 读图、显示、保存的基本操作
- 掌握图像缩放（固定尺寸 & 按比例缩放）
- 理解插值算法在缩放中的作用

#### 知识点总结
- **cv2.imread(path, flag)**：读图（flag=1彩色，0灰度）
- **img.shape**：查看图像尺寸 (H, W, C)
- **cv2.imwrite(path, img)**：保存图片
- **cv2.resize(img, (w,h), interpolation)**：固定尺寸缩放
  - `INTER_AREA`：适合缩小，平滑效果好
  - `INTER_LINEAR`：常用，适合放大
- **cv2.resize(img, None, fx, fy)**：按比例缩放
- **Matplotlib显示彩色图像时需要 BGR→RGB**：`cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`

#### 实践
1. **读图与保存**  
   - 成功读取原图并打印尺寸，保存 `hibara_copy.jpg`

2. **固定尺寸缩放**  
   - 将图像缩小至 256×256，并观察明显模糊

3. **按比例缩放**  
   - 将图像放大至 1.5 倍，尺寸变大但细节无明显增加

#### 总结
- 放大只是在像素层面插值,细节不会增加;缩小时明显模糊,说明很多像素信息被压缩了.

#### 源码
- [06-opencv_resize.py](06-opencv_resize.py)
