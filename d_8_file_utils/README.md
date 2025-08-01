## day8 📖 图像批量滤波处理

#### 目标 🎯 掌握三种常用滤波方法（blur/gaussian/median）与批量图像处理流程

#### 实践内容
- 批量读取文件夹中的图片文件
- 按需选择均值、高斯或中值滤波操作
- 可设置滤波核大小（如 3/5/7）
- 生成并保存处理后图片到指定文件夹
- 预览部分处理结果以直观感受效果

#### 知识点总结
- `cv2.blur()`：均值滤波，简单平滑图像
- `cv2.GaussianBlur()`：高斯滤波，自然平滑效果
- `cv2.medianBlur()`：中值滤波，对椒盐噪声最有效
- 文件批量处理流程、异常处理、参数化设计

#### 源码
- [08-filter_batch.py](08-filter_batch.py)
