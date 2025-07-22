import os

import pandas as  pd

#读取CSV文件
df = pd.read_csv(r'E:\files\.pycharm\ai_learning\image.csv')

print("前5行：")
print(df.head(), "\n")

print("行列数：", df.shape, "\n")

print("列名：", df.columns.tolist(), "\n")

#快速查看整个表格的结构信息
print("info():")
df.info()
print("\n")

#快速生成描述性统计信息
#默认只统计数值型列
#加上 include = 'all' 会把非数值列也统计出来
print("describe(include='all')：")
print(df.describe(include='all'), "\n")

print("label 列: ")
print(df['label'],"\n")

#df.iloc -> 按"位置"取数据
#i = index, loc = location
print("0~2行 iloc: ")
print(df.iloc[3],"\n")

#df.loc -> 按"标签/名称"取数据
print("筛选 label = cat")
print(df.loc[df['label'] == 'cat'],"\n")

print("各类别数量")
print(df['label'].value_counts(),"\n")

#拼路径并检查存在性
root_dir = r'E:\files\.pycharm\ai_learning\output_batch'
df['path'] = df['filename'].apply(lambda x: os.path.join(root_dir, x))
df['exists'] = df['path'].apply(lambda p: os.path.isfile(p))

print("带路径/存在性: ")
print(df.head(),"\n")

print("不存在的文件: ")
print(df.loc[~df['exists']],"\n")

#保存清洗结果
out_csv = r'E:\files\.pycharm\ai_learning\04-images_checked.csv'
df.to_csv(out_csv, index=False, encoding='utf-8-sig')
print("清洗后 CSV 已保存到：", out_csv)