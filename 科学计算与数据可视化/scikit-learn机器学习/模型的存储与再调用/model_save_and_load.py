# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
[illustration]

@file                : model_save_and_load.py
@version             : N/A
@interpretor         : python37_64
@modification_date   : 2020.04.20
@author              : Zhong Y. Jie
'''

import pickle
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.externals import joblib

iris = load_iris()
iris_x, iris_y = iris['data'], iris['target']

def train_model() -> SVC:
    '''训练模型'''
    clf = SVC()

    clf.fit(iris_x, iris_y) # 对模型进行训练。
    return clf

# 以下开始存储数据

def save_method_pickle(clf: SVC):
    '''使用python自带的pickle存储'''
    with open('model_save_pickle.pickle', 'wb') as fobj:
        pickle.dump(clf, fobj)
        return

def load_method_pickle() -> SVC:
    '''读取存储到pickle的模型数据'''
    with open('model_save_pickle.pickle', 'rb') as fobj:
        clf = pickle.load(fobj)
        return clf

def save_method_joblib(clf: SVC):
    '''使用sklearn所含的joblib存储模型数据。joblib采用多线程技术，对于存储大量数据更为高效。'''
    joblib.dump(clf, 'model_save_joblib.pickle')
    return

def load_method_joblib() -> SVC:
    '''用joblib读取存储的模型数据'''
    clf = joblib.load('model_save_joblib.pickle')
    return clf

if __name__ == '__main__':
    class_result = train_model()
    save_method_pickle(class_result)
    print(class_result)
    input('继续……')
    class_restore = load_method_pickle()
    print(class_result.predict(iris_x[:2]))
    print(iris_y[:2])
