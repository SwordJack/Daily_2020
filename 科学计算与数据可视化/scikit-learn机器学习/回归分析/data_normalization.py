# -*- coding: utf-8 -*-
# ./usr/bin/env python
'''
学习利用scikit-learn的数据标准化（normalization）处理以优化机器学习的成效。

@version: N/A
@interpretor: python37_64
@author: Zhong Y. Jie
@modification_date: 2020.04.19
'''

import numpy as np
from sklearn import preprocessing # 引用数据预处理模块。

a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40],], dtype=np.float64,)

print(a)
print(preprocessing.scale(a))   # preprocessing下的scale方法即为将数据标准化的方法。
