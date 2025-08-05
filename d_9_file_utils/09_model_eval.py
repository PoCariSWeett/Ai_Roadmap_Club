import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix,
                             ConfusionMatrixDisplay, classification_report,
                             roc_curve, auc, RocCurveDisplay)

# 1. 载入数据
data = load_iris()
X, y = data.data, data.target
# Iris 有 3 类；若想做 ROC 曲线，可只取前两类做二分类
# X = X[y != 2]; y = y[y != 2]

# 2. 训练/测试切分
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 3. 标准化 + 简单模型
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

clf = LogisticRegression(max_iter=200)
clf.fit(X_train_std, y_train)
y_pred = clf.predict(X_test_std)

# 4. 基本指标
acc  = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred, average='weighted')
rec  = recall_score(y_test, y_pred, average='weighted')
f1   = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy : {acc:.3f}")
print(f"Precision: {prec:.3f}")
print(f"Recall   : {rec:.3f}")
print(f"F1-score : {f1:.3f}\n")

# 5. 混淆矩阵
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=data.target_names)
disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.show()

# 6. 一键报告
print("Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# 7. 选做：ROC 曲线（仅限二分类时）
if len(np.unique(y)) == 2:
    y_score = clf.decision_function(X_test_std)
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc,
                    estimator_name="LogReg").plot()
    plt.show()
