import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#画折线图
x = [1, 2, 3, 4, 5]
y = [1,4,9,16,25]

plt.plot(x,y)
plt.title("line chart")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

#读取csv并画出柱状图
df = pd.read_csv(r'E:\files\.pycharm\ai_learning\image.csv')
counts = df['label'].value_counts()
print("类别: \n",counts)

plt.bar(counts.index,counts)
plt.title("bar chart")
plt.xlabel("category")
plt.ylabel("count")
plt.show()

#画饼图
plt.pie(counts,labels = counts.index,autopct='%1.1f%%',startangle=90)
plt.title("piechart")
plt.show()

#生成100个符合正态分布的随机数
data = np.random.random(1000)

#画直方图
plt.hist(data,
         bins=30,
         color='skyblue',
         edgecolor='pink'
         )
plt.title("Histogram")
plt.xlabel("value")
plt.ylabel("count")
plt.show()