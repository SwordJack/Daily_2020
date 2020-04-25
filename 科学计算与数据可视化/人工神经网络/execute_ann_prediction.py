# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
对自行编写的简单的神经网络进行调试。

@file                : execute_ann_prediction.py
@version             : N/A
@interpretor         : python37_64
@modification_date   : 2020.04.24
@author              : Zhong Y. Jie
'''

import pandas as pd
import numpy as np
from beginner_ann_model import BeginnerAnn
from sklearn.model_selection import train_test_split

DATA_SOURCE = pd.read_csv('data.csv')

def execute_csv_data():
    '''使用csv中的数据执行神经网络。'''
    data_input = DATA_SOURCE.iloc[:, 1:7]   # input，6列。
    data_output = DATA_SOURCE.iloc[:, 7:9]  # output，2列。
    train_input, test_input, train_output, test_output = train_test_split(data_input, data_output, test_size=10)
    ann = BeginnerAnn(eigen_value=train_input, target_value=train_output, neuron_numbers=[6, 6], standardize_data=False)
    ann.train(train_round=10000)
    print(ann.demonstrate_weights())
    print(ann.predict(test_input))
    print(test_output)

def execute_custom_data():
    '''使用自定义数据执行神经网络。'''
    # data_input = np.array([[0, 1, 0], [0, 1, 1], [0, 0, 1], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    data_input = np.array([[0, 1, 0], [0, 1, 1], [0, 0, 1], [1, 0, 0], [1, 1, 1], [0, 0, 0], [0, 1, 0]])
    data_output = np.array([[1], [0], [0], [0], [0], [0], [1]])
    ann = BeginnerAnn(eigen_value=data_input, target_value=data_output, standardize_data=False)
    ann.train(train_round=10000)
    print(ann.weights)
    print(ann.predict(np.array([[1, 1, 0], [1, 1, 1]])))

if __name__ == '__main__':
    execute_csv_data()
    # execute_custom_data()
