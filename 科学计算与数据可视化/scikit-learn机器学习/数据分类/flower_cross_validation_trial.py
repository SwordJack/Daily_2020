# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
试验不同n_neighbors参数对预测精确度的影响。
可通过sklearn.metrics.SCORERS.keys()查看评价函数的名称列表。

@file                : flower_cross_validation_trial.py
@version             : N/A
@interpretor         : python37_64
@modification_date   : 2020.04.20
@author              : Zhong Y. Jie
'''

import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets    # 引用scikit-learn的自带数据集。

from sklearn.model_selection import train_test_split, cross_val_score   # 引用训练/测试集切分和交叉验证

from sklearn.neighbors import KNeighborsClassifier  # 使用近邻算法。

iris = datasets.load_iris()  # 导入鸢尾花数据集，其中包含有data和target作为键的字典。

iris_x = iris['data']       # 花的属性。
iris_y = iris['target']     # 花的分类。

k_range = range(1, 31)
k_loss_scores = list()  # 记录不同n_neighbors参数得到的均方误差大小
for i in k_range:
    knn = KNeighborsClassifier(n_neighbors=i)
    # scores = cross_val_score(
    #     estimator=knn,      # 使用的模型是knn
    #     X=iris_x,           # 自变量是iris_x 
    #     y=iris_y,           # 因变量是iris_y
    #     cv=5,               # 划分为5组
    #     scoring='accuracy', # 指定其评价函数，如accuracy、roc_auc等
    # )
    loss = -cross_val_score(    # 交叉验证，得到均方误差。
        estimator=knn,
        X=iris_x,
        y=iris_y,
        cv=10,
        scoring='neg_mean_squared_error'    # 指定均方误差为评价函数，其调用不再是'mean_squared_error'。
    )
    k_loss_scores.append(loss.mean())
    continue

plt.plot(k_range, k_loss_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross Validated Accuracy')
plt.show()