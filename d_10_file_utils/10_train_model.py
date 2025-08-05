import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, ConfusionMatrixDisplay)
from sklearn.neighbors import KNeighborsClassifier
import joblib
import matplotlib.pyplot as plt

csv_path = r'E:\files\.pycharm\ai_learning\10-image_features.csv'
df = pd.read_csv(csv_path)

X = df[['filename', 'std', 'aspect']].values
y = df['label'].values
print("样本数:", X.shape[0], "特征维度:", X.shape[1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

clf = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
clf.fit(X_train, y_train)

cv_scores = cross_val_score(clf, X_train, y_train, cv=5)
print("CV mean acc:", cv_scores.mean().round(3))

y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred).round(3))
print("\nClassification report:\n",
      classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred, labels=np.unique(y))
disp = ConfusionMatrixDisplay(cm, display_labels=np.unique(y))
disp.plot(cmap='Blues')
plt.title("Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_day10.png")
plt.show()

model_path = "knn_model.joblib"
joblib.dump(clf, model_path)
print(f"模型已保存 → {model_path}")

loaded_clf = joblib.load(model_path)
print("加载模型后再次预测，Acc:",
      accuracy_score(y_test, loaded_clf.predict(X_test)).round(3))
