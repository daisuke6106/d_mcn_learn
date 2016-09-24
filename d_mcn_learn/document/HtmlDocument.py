'''
Created on 2016/09/22

@author: dk
'''
# -*- coding: utf-8 -*-

import glob

from bs4 import BeautifulSoup

class HtmlDocument(object):
    
    @staticmethod
    def getHtmlByDir(path):
        files = glob.glob(path)
        list  = []
        for file in files:
            list.append(HtmlDocument(open(file).read()))
            
        return list
        
    def __init__(self, data):
        '''
        Constructor
        
        :param data: Html
        '''
        self.data = data
        self.bs = BeautifulSoup(data)
    
    def get_title(self):
        return self.bs.find('title').text