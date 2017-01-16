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
    def sample_data(from_num = -1.0, to_num = 1.0, inc = 0.1):
        return Array(np.arange(from_num, to_num, inc))

    @staticmethod
    def dot(array1, array2):
        return Array(np.dot(array1, array2))
        
    def sigmoid(self):
        result = Array(Array._sigmoid(self.arrays))
        return ResultArrays(self, result)
    
    @staticmethod
    def _sigmoid(array):
        return 1 / (1 + np.exp(-array))
    
    def relu(self):
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
    