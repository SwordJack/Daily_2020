# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
python使用Auto ARIMA构建高性能时间序列模型
https://blog.csdn.net/m0_37700507/article/details/84855235
CC 4.0 BY-SA

@file                : arima_prediction.py
@version             : N/A
@interpretor         : python37_64
@modification_date   : 2018.12.16
@author              : python语音识别-公众号
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pmdarima import auto_arima

#load the data

data = pd.read_csv('international-airline-passengers.csv')

#divide into train and validation set
train = data[:int(0.7*(len(data)))]
valid = data[int(0.7*(len(data))):]
 
#preprocessing (since arima takes univariate series as input)
train.drop('Month',axis=1,inplace=True)
valid.drop('Month',axis=1,inplace=True)

#plotting the data
train['International_airline_passengers'].plot()
valid['International_airline_passengers'].plot()
# plt.plot(train['Month'], train['International_airline_passengers'], color='blue')
# plt.plot(valid['Month'], valid['International_airline_passengers'], color='orange')
# plt.show()


#building the model
# model = auto_arima(train, trace=True, error_action='ignore', suppress_warnings=True)
model = auto_arima(train)
model.fit(train)
 
forecast = model.predict(n_periods=len(valid))
forecast = pd.DataFrame(forecast,index = valid.index,columns=['Prediction'])
 
#plot the predictions for validation set
plt.plot(train, label='Train')
plt.plot(valid, label='Valid')
plt.plot(forecast, label='Prediction')
plt.show()

#calculate rmse
from math import sqrt
from sklearn.metrics import mean_squared_error
 
rms = sqrt(mean_squared_error(valid,forecast))  # 均方根误差。
print(rms)