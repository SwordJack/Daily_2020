# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
用于生成满足一定条件的数据，并将之放入data.csv文件中

@file                : generate_data.py
@version             : N/A
@interpretor         : python37_64
@modification_date   : 2020.04.24
@author              : Zhong Y. Jie
'''

import numpy as np
import pandas as pd
from random import randint

DATA_SOURCE = pd.read_csv('data.csv')
data_columns = DATA_SOURCE.columns.values.tolist()

data_scale = 100

data_group = dict()
input_value_group = list()
for column in data_columns:
    if column == 'index':
        data_group[column] = pd.Series([x+1 for x in range(data_scale)])
    elif 'input' in column:
        data_group[column] = pd.Series([randint(0, 1) for x in range(data_scale)])
        input_value_group.append(data_group[column].tolist())
    elif 'output' in column:
        if column == 'output_0':
            data_group[column] = pd.Series([int([row[x] for row in input_value_group].count(1) >= 3) for x in range(data_scale)])
        elif column == 'output_1':
            data_group[column] = pd.Series([int([row[x] for row in input_value_group].count(1) < 5) for x in range(data_scale)])
    continue
data_table = pd.DataFrame(data_group)
data_table.to_csv('data.csv', index=False)
