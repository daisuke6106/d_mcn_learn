'''
Created on 2017/01/13

@author: dk
'''

import numpy as np
import matplotlib.pylab as plt

class Array(object):

    def __init__(self, arrays):
        '''
        Constructor
        '''
        self.arrays = arrays

    @staticmethod
    def create_array(array):
        return Array(np.array(array))
    
    @staticmethod
    def sample_data(from_num = -1.0, to_num = 1.0, inc = 0.1):
        return Array(np.arange(from_num, to_num, inc))

    def dot(self, array):
        u"""
        この行列と引数に指定された行列の積を求め、返却する。
        """
        return Array._dot(self.arrays, array.arrays)
        
    @staticmethod
    def _dot(array1, array2):
        return Array(np.dot(array1, array2))
        
    def sigmoid(self):
        u"""
        この行列にシグモイド関数を実行し、その結果を返却する。
        """
        result = Array(Array._sigmoid(self.arrays))
        return ResultArrays(self, result)
    
    @staticmethod
    def _sigmoid(array):
        return 1 / (1 + np.exp(-array))
    
    def relu(self):
        u"""
        この行列にRelu関数を実行し、その結果を返却する。
        """
        result = Array(Array._relu(self.arrays))
        return ResultArrays(self, result)
    
    @staticmethod
    def _relu(array):
        return np.maximum(0, array)
    
    def ndim(self):
        u""" 
             次元数を取得する。
        """
        return np.ndim(self.arrays)
    
    def shape(self):
        u""" 
             行列の形状を取得する。
        """
        return self.arrays.shape
        
    def softmax(self):
        u""" 
             ソフトマックス関数の実施結果を返却する。
        """
        
        # オーバーフロー対策の為、入力信号の中で最大値を差し引く
        maxum = np.max(self.arrays)
        exp_a = np.exp(self.arrays - maxum)
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a
        return y
        
class ResultArrays(object):
    '''
    classdocs
    '''
    def __init__(self, before_array, after_array):
        '''
        Constructor
        '''
        self.before = before_array
        self.after  = after_array

    def plot(self, y_min = -1.0, y_max = 1.0, x_min = -1.0, x_max = 1.0):
        x = self.before.arrays
        y = self.after.arrays
        plt.plot(x, y)
        plt.ylim(y_min, y_max)
        plt.xlim(x_min, x_max)
        plt.show()
    