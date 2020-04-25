# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
学习利用scikit-learn内置波士顿房价数据集进行机器学习的线性回归分析。

@version: N/A
@interpretor: python37_64
@author: Zhong Y. Jie
@modification_date: 2020.04.19
'''

import numpy as np
from sklearn import datasets    # 引用scikit-learn的自带数据集。

from sklearn.linear_model import LinearRegression  # 使用线性回归算法。

loaded_data = datasets.load_boston()
data_x = loaded_data['data']
data_y = loaded_data['target']

print(data_x[:1, :])
#print(data_y)

model = LinearRegression()
model.fit(data_x, data_y)
#print('线性回归的预测结果：\n', model.predict(data_x[:4, :]), sep='')
#print('真实值的结果：\n', data_y[:4], sep='')
print(model.coef_)          # 输出系数。
print(model.intercept_)     # 输出截距。
print(model.score(data_x, data_y))  # 输出R^2
