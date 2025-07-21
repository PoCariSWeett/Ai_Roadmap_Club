## day3📖 Numpy与图像矩阵操作

#### 学习内容
- 初步掌握 Numpy 的基础使用：
  - 创建数组（`np.zeros`, `np.ones`, `np.arange`）
  - 基本属性（`shape`, `dtype`）
  - 索引与切片（如 `a[2,2]`、`a[0:2,1:3]`）

- 通过 OpenCV 读取图像，理解图像其实就是一个 Numpy 的三维数组 `(H, W, C)`：
  - H 表示高度（行数）
  - W 表示宽度（列数）
  - C 表示通道数（BGR三个颜色通道）

- 图像像素操作：
  - 单像素修改（例如 `img[50,50] = [0,0,255]` 把一个点改成红色）
  - 区域修改（例如 `img[0:100,0:100]` 改一个区域的颜色）

- 矩阵运算：
  - 调亮：`np.clip(img + 50, 0, 255)`
  - 负片：`255 - img`

#### 实践代码👩‍💻
- [numpy+图像读取](03-numpy_image.py)
- [numpy快速体验](03-numpy_practice.py)
- [图像矩阵基本属性](03-numpy_practice2.py)
- [区域操作](03-numpy_practice3.py)
- [矩阵运算做图像处理](03-numpy_practice4.py)
