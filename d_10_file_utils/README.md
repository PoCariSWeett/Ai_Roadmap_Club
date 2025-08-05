## day10  模型训练与保存

#### 目标 
- 选用 **KNN / SVM / RF** 等传统分类器  
- 使用 Pipelines → 标准化 + 模型  
- 交叉验证 `cross_val_score` 评估稳定性  
- 输出混淆矩阵、分类报告  
- 学会 `joblib.dump / load` 保存与加载模型

#### 实践流程
1. **数据准备**：从 `image_features.csv` 读取 3 个简单特征 + label  
2. **train_test_split** (`test_size=0.2, stratify=y`)  
3. **模型**：`Pipeline(StandardScaler → KNeighborsClassifier)`  
4. **交叉验证**：5-fold，CV-mean≈ …  
5. **评估**：Accuracy = … ，详见 `confusion_day10.png`  
6. **模型持久化**：`knn_model.joblib`  
7. **加载验证**：加载模型后 Accuracy 与原评估一致

#### 源码
- [`10_train_model.py`](10_train_model.py)
