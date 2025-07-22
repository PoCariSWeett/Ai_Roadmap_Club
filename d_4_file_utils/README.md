## day4📖 Pandas表格读取与数据统计

#### 目标🤺
- 学会使用 Pandas 读取 CSV 文件并查看表格数据
- 掌握常用的表格操作：查看数据、列/行访问、条件筛选
- 能够统计类别数量，为后续训练模型做数据准备
- 能为每条数据拼接完整文件路径，并检查文件是否存在

#### 知识点总结🌸
- **pd.read_csv(path)**：读取 CSV 文件为 DataFrame
- **df.head() / df.tail()**：查看前几行 / 后几行
- **df.shape / df.info()**：查看行列数、每列数据类型、缺失值
- **df.describe(include='all')**：生成各列的描述性统计（包括分类列）
- **df.iloc / df.loc**：
  - iloc：按整数位置索引
  - loc：按标签或条件索引
- **df['列名'].value_counts()**：统计每个类别的数量
- **df.apply(lambda x: ...)**：对某列的每个元素应用函数
- **os.path.join()**：拼接完整路径
- **os.path.isfile()**：检查文件是否存在
- **df.to_csv(path, index=False, encoding='utf-8-sig')**：保存处理好的表格，utf-8-sig防止中文乱码

#### 源码👩‍🌾
- [04-pandas_basis.py](04-pandas_basis.py)
