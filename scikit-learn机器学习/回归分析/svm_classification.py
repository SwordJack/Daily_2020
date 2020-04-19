# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
学习利用scikit-learn的SVM进行数据分类的操作。

@version: N/A
@interpretor: python37_64
@author: Zhong Y. Jie
@modification_date: 2020.04.19
'''

import numpy as np
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification    # make_classification方法现今存在于datasets模块中。
from sklearn.svm import SVC


x, y = make_classification(
    n_samples=300,      # 300个样本
    n_features=2,       # 2个属性
    n_redundant=0,      # 0个冗余
    n_informative=2,    # 2个相关属性（在这里即说明两个属性是相关的）
    random_state=22,    # 随机数种子
    n_clusters_per_class=1,     # 每个类的集群数量
    scale=100,                  # 将样本值乘以scale
)

# plt.scatter(x[:, 0], x[:, 1], c=y)
# plt.show()

# x = preprocessing.minmax_scale(
#     x,
#     feature_range=(0, 1)    # 将数据标准化到0~1的范围。
# )

x = preprocessing.scale(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
clf = SVC()
clf.fit(X=x_train, y=y_train)
print(clf.score(x_test, y_test))
