'''
Created on 2017/01/13

@author: dk
'''

import numpy as np
import matplotlib.pylab as plt

class Array(object):
    '''
    classdocs
    '''
    def __init__(self, arrays):
        '''
        Constructor
        '''
        self.arrays = arrays
        
        
    def sigmoid(self):
        return 1 / (1 + np.exp(-self.arrays))
    
    def sigmoid_plot(self):
        x = self.arrays
        y = self.sigmoid()
        plt.plot(x, y)
        plt.show()
    
    @staticmethod
    def sample_data(from_num = -1.0, to_num = 1.0, inc = 0.1):
        return Array(np.arange(from_num, to_num, inc))
    