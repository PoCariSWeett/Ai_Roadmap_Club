## day5📖 图像文件读取工具总结

#### 目标🤺 
- 学习 Matplotlib 的基本用法
- 会用柱状图、饼图、直方图展示数据分布
- 结合 Pandas 统计结果，完成对图片类别的可视化

#### 知识点总结🐣
- **plt.plot(x, y)**：折线图
- **plt.bar(x, height)**：柱状图
- **plt.pie(values, labels, autopct)**：饼图（autopct='%1.1f%%'显示百分比）
- **plt.hist(data, bins)**：直方图
- **plt.title / plt.xlabel / plt.ylabel**：添加标题和坐标轴说明
- **plt.show()**：显示图像
- **plt.savefig("xxx.png")**（可选）：保存图像

#### 实践总结
1. **折线图**  
   - 用示例数据 `[1,4,9,16,25]` 画简单折线

2. **柱状图**  
   - 用 Pandas `value_counts()` 统计各类别图片数量
   - 一行代码生成柱状图，清晰展示各类别数量

3. **饼图**  
   - 同样用 `value_counts()`，显示各类别所占百分比

4. **直方图**（选做）  
   - 生成1000个随机数，画出钟形分布直方图
  
#### 源码📕
👉[05-matplotlib_datavisualize.py](05-matplotlib_datavisualize.py)
