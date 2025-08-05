## day9  模型评估基础

#### 目标 
- 了解并使用常见分类评估指标  
  `Accuracy / Precision / Recall / F1`
- 学会绘制 Confusion Matrix，并阅读四象限
- 一键输出 `classification_report`
- 选做：掌握二分类 `ROC & AUC` 曲线

#### 实践步骤
1. `train_test_split` 划分训练 / 测试集  
2. 训练 `LogisticRegression`（或任意分类器）  
3. 计算四大指标并解释各自含义  
4. 可视化 **Confusion Matrix**  
5. 打印 `classification_report`  
6. *二分类选做*：绘制 **ROC 曲线** 并计算 AUC

#### 产出
- 终端打印四大指标 + classification_report  
- `confusion_matrix.png`（截图或 `plt.savefig`）  
- （选做）`roc_curve.png`

#### 源码
- [09_model_eval.py](09_model_eval.py)
