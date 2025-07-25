## day2📖 图像预处理(单张图片+批量处理)

#### 目标🤺
- 学习 Python 图像处理常用库: OpenCV(cv2) + Matplotlib
- 完成基本图像操作: 读取 / 灰度化 / 缩放 / 显示 / 保存

#### 知识点总结👩‍🌾
- **cv2.imread(path)**：读取图片（注意 OpenCV 默认是 BGR 格式）
- **cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)**：彩色 → 灰度
- **cv2.resize(img, size)**：调整图片尺寸，size=(width,height)
- **cv2.imwrite(path, img)**：保存图片
- **matplotlib.pyplot.imshow()**：显示图片（需将 BGR 转为 RGB）
- **os、glob**：文件路径处理，批量读取文件

#### 源码
- [初始版本(只能处理单张图片)](02-img_preprocess.py)
- [改进版本 --> 增加批量处理](02-img_preprocess_2.py)
  - 主要改进:
  - - ✅ **增加批量处理功能**：支持文件夹输入，自动创建输出目录
  - - ✅ **处理中文/带引号路径**：输入时自动 strip 引号
  - - ✅ **增加失败处理**：无法读取或保存时给出提示，不影响其他文件
  - - ✅ **预览前 N 张图片**：防止大批量图片显示卡死
  - - ✅ **自动命名输出文件**：原名 + `_gray` 后缀，避免覆盖
  - - ✅ **统计处理结果**：打印成功 / 失败数量，便于检查
