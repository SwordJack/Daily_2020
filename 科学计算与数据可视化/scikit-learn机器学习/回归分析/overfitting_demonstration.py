# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
演示过拟合对预测精度的影响。

@file                : overfitting_demonstration.py
@version             : N/A
@interpretor         : python37_64
@modification_date   : 2020.04.20
@author              : Zhong Y. Jie
'''

from sklearn.model_selection import learning_curve, validation_curve    # 引用学习曲线
from sklearn.datasets import load_digits                                # 引用数字数据集
from sklearn.svm import SVC                                             # 支持向量机分类
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
X = digits['data']
y = digits['target']

# train_sizes, train_loss, test_loss = learning_curve(    # 学习曲线，输出训练规模、（随时间变化的）训练误差值、测试误差值。
#     estimator=SVC(
#         gamma=0.001 # gamma值表示的是数据映射到新的特征空间后的分布，gamma值越大，支持向量就越少，gamma值越小，支持向量就越多。支持向量的个数影响训练与预测的速度。
#         # gamma=0.01  # 此时会引发过拟合，训练集误差很低，但是测试集的误差下不来。
#     ),
#     X=X,
#     y=y,
#     cv=10,
#     scoring='neg_mean_squared_error',       # 使用的评价函数。
#     train_sizes=[0.1, 0.25, 0.5, 0.75, 1]   # 记录误差值的进度点。
# )

param_range = np.logspace(-6, -2.3, 5)      # 返回在-6～-2.3范围内在对数上等距离的5个点。
train_loss, test_loss = validation_curve(   # 验证曲线，输出（随时间变化的）训练误差值、测试误差值。
    estimator=SVC(),
    X=X,
    y=y,
    param_name='gamma',
    param_range=param_range,    # 通过param_range改变gamma的值，观察不同gamma值对预测精度的影响。
    cv=10,
    scoring='neg_mean_squared_error',       # 使用的评价函数。
)

train_loss_mean = -np.mean(train_loss, axis=1)  # loss值是负数，取相反数将其变为正数，按列取值。
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(
    #train_sizes,        # 训练的长度。
    param_range,        # 横坐标不再是train_sizes而是param_range
    train_loss_mean,    # 每一步训练的均方误差平均值。
    'o-',
    color='red',
    label='Training'
)

plt.plot(
    #train_sizes,
    param_range,
    test_loss_mean,
    'o-',
    color='green',
    label='Cross-Validation'
)

plt.xlabel('Training examples')     # 横坐标
plt.ylabel('Loss')                  # 纵坐标
plt.legend(loc='best')
plt.show()
