# -*- coding: utf-8 -*-
# !/usr/bin/env python
'''
利用scikit-learn内置鸢尾花数据集学习交叉验证。

@version: N/A
@interpretor: python37_64
@author: Zhong Y. Jie
@modification_date: 2020.04.20
'''

import numpy as np
from sklearn import datasets    # 引用scikit-learn的自带数据集。

# sklearn.cross_validation在scikit-learn的1.9版本后被弃用，以model_selection代替之。
from sklearn.model_selection import train_test_split, cross_val_score   # 引用训练/测试集切分和交叉验证

from sklearn.neighbors import KNeighborsClassifier  # 使用近邻算法。

iris = datasets.load_iris()  # 导入鸢尾花数据集，其中包含有data和target作为键的字典。

iris_x = iris['data']       # 花的属性。
iris_y = iris['target']     # 花的分类。

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(
    estimator=knn,      # 使用的模型是knn
    X=iris_x,           # 自变量是iris_x 
    y=iris_y,           # 因变量是iris_y
    cv=5,               # 划分为5组
    scoring='accuracy', # 指定其评价函数，如accuracy、roc_auc等
)
print(scores)