# -*- encoding: utf-8 -*-
# !/usr/bin/env python
'''
学习并尝试编写的一个人工神经网络模型。

@file                : beginner_ann_model.py
@version             : N/A
@interpretor         : python37_64
@modification_date   : 2020.04.24
@author              : Zhong Y. Jie
'''

from numpy import array, exp, dot       # 引用数组、e底数幂、点乘。
from numpy import random as np_random   # 引用numpy中的随机数
from sklearn.preprocessing import StandardScaler        # 引用数据标准化模块。

class BeginnerAnn():
    '''一个基础的神经网络类。
    param eigen_value: 输入的特征值（可理解为用于训练的X轴数据）
    param target_value: 输出的目标值（可理解为用于训练的Y轴数据）
    param neuron_numbers: 隐藏层神经元数量（列表形式），默认为单神经元
    param standardize_data: 是否要将数据进行标准化（默认为否）'''

    def __init__(self, eigen_value, target_value, neuron_numbers: list = None, standardize_data: bool = False):
        '''BeginnnerAnn类的构造函数
        param eigen_value: 输入的特征值（可理解为用于训练的X轴数据）
        param target_value: 输出的目标值（可理解为用于训练的Y轴数据）
        param neuron_numbers: 隐藏层神经元数量（列表形式），默认为单神经元
        param standardize_data: 是否要将数据进行标准化（默认为否）'''
        self.standardize_data = standardize_data
        if standardize_data:
            self.ss_x = StandardScaler()    # 用于将X数据标准化。
            self.ss_y = StandardScaler()    # 用于将Y数据标准化。
            self.train_eigen_value = self.ss_x.fit_transform(eigen_value)
            self.train_target_value = self.ss_y.fit_transform(target_value)
        else:
            self.train_eigen_value = eigen_value
            self.train_target_value = target_value
        self.hidden_layer_neuron_numbers = neuron_numbers
        if neuron_numbers is not None:
            self.weights_list = list()
            for i in range(0, len(neuron_numbers)):   # 对于神经元数目列表中的每一层。
                if i == 0:
                    self.weights_list.append(np_random.random((eigen_value.shape[1], neuron_numbers[i])) * 2 - 1)   # 第0隐藏层，特征值向第0层的神经元映射。
                else:
                    self.weights_list.append(np_random.random((neuron_numbers[i-1], neuron_numbers[i])) * 2 - 1) # 之后的隐藏层，是由上一层的神经元向本层映射。
            self.weights_list.append(np_random.random((neuron_numbers[-1], target_value.shape[1])) * 2 - 1)  # 输出层，neuron_number个神经元向输出数据的神经元映射。
        if (neuron_numbers is None):                                    # 给单神经元赋以初始权重。
            self.weights = np_random.random((eigen_value.shape[1], 1)) * 2 - 1
        if (neuron_numbers is None and target_value.shape[1] != 1):     # 单个神经元无法进行多个输出。
            raise RuntimeError('单个神经元无法进行多个输出。')

    def forward_propagate(self, eigen_value, weights_list):
        '''正向传播，对输入的X和权重值计算得到输出。
        param eigen_value: 传入的特征（自变量）值
        param weights_list: 传入的权重值列表（一层为一项）'''
        # '''正向传播，对输入的X和权重值计算得到输出。
        # param eigen_value: 传入的特征（自变量）值
        # param weights: 传入的权重值'''
        # z = dot(eigen_value, weights)   # 利用矩阵点乘一次性计算一列z值。
        # output = 1/(1+exp(-z))          # 使用Sigmoid函数，输出当次传播的结果。
        # return output
        current_eigen_value = eigen_value   # 当前特征值，初始设定为传入的特征值；之后每一层正向传播的输出值会改换为下一层的特征值。
        output_list = list()                # 记录每一层的输出结果。
        
        if type(weights_list) != list:      # 如传入的权重值列表不为列表类型（说明只有单个神经元，即只有一组权重），
            weights_list = [weights_list]   # 则将其调整为列表类型以利之后的计算。
        
        for weights in weights_list:
            # print(weights)
            z = dot(current_eigen_value, weights)   # 利用矩阵点乘一次性计算一列z值。
            current_output = 1/(1+exp(-z))          # 使用Sigmoid函数，输出当前层正向传播的结果。
            current_eigen_value = current_output    # 当前特征值改换为当前层的输出。
            output_list.append(current_output)      # 在输出列表中添加当前层输出的结果。
        if len(output_list) > 1:    # 如果输出了多层结果，则返回结果列表。
            return output_list
        else:                       # 如果仅输出了一层结果，返回当层结果即可。
            return output_list[0]

    def backward_propagate(self, output_list, target_value, weights_list=None):
        '''反向传播，根据正向传播的输出值和目标值进行比较，从而返回需要进行调整的增量大小。
        param output_list: 正向传播每层的输出值
        param target_value: 目标值'''
        # '''反向传播，根据正向传播的输出值和目标值进行比较，从而返回需要进行调整的增量大小。
        # param output_value: 正向传播的输出值
        # param target_value: 目标值'''
        # error_value = target_value - output_value   # 计算得到输出值与目标值的误差。
        # slope = output_value * (1 - output_value)   # 计算斜率（梯度下降，愈接近，则增速应越慢。）
        # delta = error_value * slope                 # 计算增量
        # return delta
        if type(output_list) != list:       # 如传入的output_list不为列表类型（说明只有单个神经元，即只有一组权重），则按照单个神经元的方式进行处理。
            output_value = output_list
            error_value = target_value - output_value   # 计算得到输出值与目标值的误差。
            slope = output_value * (1 - output_value)   # 计算斜率（梯度下降，愈接近，则增速应越慢。）
            delta = error_value * slope                 # 计算增量
            return delta
        else:
            delta_list_reverse = list()                 # 倒序的调整值列表。
            output_list_reverse = output_list[::-1]     # 将输出表倒序，从后向前传播。
            # print(type(output_list_reverse))
            output_list_length = len(output_list)       # 输出表的长度。
            weights_list_reverse = weights_list[::-1]   # 将权重值表倒序。
            current_target = target_value               # 当前目标值，初始设定为传入的最终目标值；每一层输出值会被作为其前一层的目标值。
            for i in range(0, output_list_length):
                slope = output_list_reverse[i] * (1 - output_list_reverse[i])   # 计算坡度。
                if i == 0:      # 对于最后一层（输出层），将其根据目标值进行调整。
                    current_error = current_target - output_list_reverse[i]     # 与目标进行比对获得误差值。
                else:
                    current_error = dot(delta_list_reverse[i-1], (weights_list_reverse[i-1]).T) # 根据后一层的调整值，乘以权重，产生当前层误差值。
                delta_list_reverse.append(current_error * slope)
            delta_list = delta_list_reverse[::-1]       # 将倒序的调整值列表倒过来。
            return delta_list

    def mononeuron_training(self, train_round: int = 5000):
        '''尝试用单个神经元进行预测计算。
        param train_round: 训练的次数，默认为5000次。'''
        # train_X, train_Y, predict_X = self.data_preprocessing(region_key=region_key) # 加载数据。

        # ss_x = StandardScaler()     # 用于将X数据标准化。
        # ss_y = StandardScaler()     # 用于将Y数据标准化。
        # train_X_standard = ss_x.fit_transform(train_X)      # 将训练集X数据标准化。
        # predict_X_standard = ss_x.fit_transform(predict_X)  # 将预测集X数据标准化。
        # train_Y_standard = ss_y.fit_transform(train_Y)
        train_X_standard = self.train_eigen_value
        train_Y_standard = self.train_target_value

        # print(train_X_standard)
        # print(train_Y_standard)
        # print(ss_y.inverse_transform(train_Y_standard))
        # input()

        #3. 设置随机权重
        # weights = np_random.random((train_X_standard.shape[1], 1)) * 2 - 1

        #4. 循环
        for it in range(train_round):

            # 正向传播，计算输出。
            output = self.forward_propagate(
                eigen_value=train_X_standard,
                weights_list=self.weights)
            
            delta = self.backward_propagate(     # 反向传播，计算增量。
                output_list=output,
                target_value=train_Y_standard,
            )

            self.weights += dot(train_X_standard.T, delta)   # 更新权重
            continue
        
        # train_Y_result = ss_y.inverse_transform(self.forward_propagate(eigen_value=train_X_standard, weights_list=weights))


        # predict_Y_standard = self.forward_propagate(predict_X_standard, weights_list=weights)
        # predict_Y = ss_y.inverse_transform(predict_Y_standard)

        # print('{}地区权重：\n{}；'.format(REGION_DICT[region_key], weights))
        # print('训练结果：\n{}；'.format(train_Y_result))
        # print('预测结果：\n{}；'.format(predict_Y))
        # print('===========================================================')
        # input()

    def multilayer_neuron_training(self, train_round: int = 5000):
        '''尝试用多层神经元进行预测计算
        param train_round: 训练的次数，默认为5000'''
        # param neuron_numbers: 隐藏层神经元数量（列表形式）。'''

        # 获取数据
        # train_X, train_Y, predict_X = self.data_preprocessing(region_key=region_key)

        # 进行数据标准化处理。
        # ss_x = StandardScaler()
        # ss_y = StandardScaler()
    
        # train_X_standard = ss_x.fit_transform(train_X)
        # train_Y_standard = ss_y.fit_transform(train_Y)
        # predict_X_standard = ss_x.fit_transform(predict_X)

        train_X_standard = self.train_eigen_value
        train_Y_standard = self.train_target_value

        # # 分配初始权重，经过处理使权重分布在-1~1之间。
        # weights_list = list()
        # for i in range(0, len(neuron_numbers)):   # 对于神经元数目列表中的每一层。
        #     if i == 0:
        #         weights_list.append(np_random.random((train_X_standard.shape[1], neuron_numbers[i])) * 2 - 1)   # 第0隐藏层，特征值向第0层的神经元映射。
        #     else:
        #         weights_list.append(np_random.random((neuron_numbers[i-1], neuron_numbers[i])) * 2 - 1) # 之后的隐藏层，是由上一层的神经元向本层映射。
        # weights_list.append(np_random.random((neuron_numbers[-1], train_Y_standard.shape[1])) * 2 - 1)  # 输出层，neuron_number个神经元向输出数据的神经元映射。

        for i in range(train_round):  # 将数据投入循环计算。
            layer_output_list = self.forward_propagate( # 获取正向传播的输出值（第一个隐藏层到输出层）。
                eigen_value=train_X_standard,
                weights_list=self.weights_list)

            delta_list = self.backward_propagate(    # 获取调整值。
                output_list=layer_output_list,
                target_value=train_Y_standard,
                weights_list=self.weights_list
            )
            # print(delta_list)
            # input()

            # print(len(weights_list))
            # print(len(delta_list))
            # input()
            for j in range(0, len(self.weights_list)):
                if j == 0:
                    self.weights_list[j] += dot(train_X_standard.T, delta_list[j])
                else:
                    self.weights_list[j] += dot(layer_output_list[j-1].T, delta_list[j])

        # train_Y_result_standard = self.forward_propagate(eigen_value=train_X_standard, weights_list=weights_list)[-1]    # 只需要最后的输出项。
        # train_Y_result = ss_y.inverse_transform(train_Y_result_standard)
        # predict_Y_standard = self.forward_propagate( 
        #     eigen_value=predict_X_standard,
        #     weights_list=weights_list,
        # )[-1]
        # predict_Y = ss_y.inverse_transform(predict_Y_standard)
        # print('权重：')
        # for i in range(0, len(weights_list)):
        #     print('第{0}层：\n{1}'.format(i+1, weights_list[i]))
        # print('------------------------最后一层是输出的结果-------------------------')
        # print('训练结果：\n{}；\n-------------------------------------------------'.format(train_Y_result))
        # print('预测结果：\n{}；'.format(predict_Y))
        # print('===========================================================')

    def train(self, train_round: int=5000):
        '''对神经网络进行训练
        param train_round: 训练次数'''
        if self.hidden_layer_neuron_numbers is not None:        # 含隐藏层的神经网络。
            self.multilayer_neuron_training(train_round=train_round)
        else:   # 不含隐藏层的单神经元。
            self.mononeuron_training(train_round=train_round)

    def predict(self, eigen_value):
        '''进行数据预测
        param eigen_value: 传入的待预测的特征值。'''
        if self.standardize_data:   # 如果选择了数据需要标准化，则也要标准化此时用于预测的输入值。
            eigen_value_standard = self.ss_x.fit_transform(eigen_value)
        else:       # 如果选择了不标准化，此时也不执行标准化。
            eigen_value_standard = eigen_value
        
        result = array([])
        if self.hidden_layer_neuron_numbers is not None:        # 含隐藏层的神经网络。
            result = self.forward_propagate(eigen_value=eigen_value_standard, weights_list=self.weights_list)[-1]
        else:   # 不含隐藏层的单神经元。
            result = self.forward_propagate(eigen_value=eigen_value_standard, weights_list=self.weights)
        
        if self.standardize_data:   # 如果选择了数据需要标准化，则也要还原输出值。
            return self.ss_y.inverse_transform(result)
        else:       # 如果选择了不标准化，此时也不执行标准化数据的还原。
            return result

    def demonstrate_weights(self):
        '''返回一个字符串，显示权重情况。'''
        if self.hidden_layer_neuron_numbers is not None:
            demonstration_string = '''===========================================
神经网络含有{0}个隐藏层，各隐藏层神经元个数为{1}。
-------------------------------------------
各层权重情况：
'''.format(len(self.hidden_layer_neuron_numbers), '、'.join([str(number) for number in self.hidden_layer_neuron_numbers]))
            for i in range(len(self.weights_list)):
                demonstration_string += '第{0}层：\n{1}；\n'.format(i+1, self.weights_list[i])
                continue
            demonstration_string += '==========================================='
            return demonstration_string
        else:
            demonstration_string = '''===========================================
单个神经元。
-------------------------------------------
权重情况：
{}
==========================================='''.format(len(self.weights))
            return demonstration_string

if __name__ == '__main__':
    # mononeuron_prediction(region_key=key)
    # multilayer_neuron_training(region_key=key, neuron_numbers=[5, 6, 4])
    pass
