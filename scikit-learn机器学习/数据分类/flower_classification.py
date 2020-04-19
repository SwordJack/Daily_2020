# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
学习利用scikit-learn内置鸢尾花数据集进行机器学习分类。

@version: N/A
@interpretor: python37_64
@author: Zhong Y. Jie
@modification_date: 2020.04.19
'''

import numpy as np
from sklearn import datasets    # 引用scikit-learn的自带数据集。

# sklearn.cross_validation在scikit-learn的1.9版本后被弃用，以model_selection代替之。
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier  # 使用近邻算法。

iris = datasets.load_iris()  # 导入鸢尾花数据集，其中包含有data和target作为键的字典。

iris_x = iris['data']       # 花的属性。
iris_y = iris['target']     # 花的分类。

#print(iris_x[:2, :])    # 打印花属性的前两组，每组是一个含有4个元素的列表。
#print(iris_y)           # 打印花分类的数据（若干的0、1、2）。

x_train, x_test, y_train, y_test = train_test_split(    # 对数据集进行打乱、切分，并设置测试集的比例为
    iris_x, iris_y, test_size=0.3
)

#print(y_test)   # 测试集的y数据，已经进行了打乱。

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

print('knn预测的结果：\n', knn.predict(x_test), sep='')
print('真实结果：\n', y_test, sep='')
