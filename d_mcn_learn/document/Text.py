'''
Created on 2016/09/25

@author: dk
'''

# -*- coding: utf-8 -*-

import os
import re
import MeCab

from sklearn.feature_extraction.text import TfidfVectorizer

class Text(object):
    '''
    classdocs
    '''
    
    @staticmethod
    def get_text_by_dir(directory, filename):
        return Text._get_text_by_dir(directory, filename, lambda text : Text(text))
    
    @staticmethod
    def _get_text_by_dir(directory, filename, creater_func):
        textlist = []
        for file in Text._fild_all_files(directory, filename):
            filestr = ''
            for line in open(file, 'r'):
                filestr += line.rstrip()
            textlist.append(creater_func(filestr))
        return textlist
    
    @staticmethod
    def _fild_all_files(directory, filename):
        pattern = re.compile(filename)
        for root, _, files in os.walk(directory):
            for file in files:
                is_match = pattern.match(file)
                if is_match :
                    yield os.path.join(root, file)
                    
    def __init__(self, text):
        '''
        Constructor
        :param text: テキスト
        '''
        self.origin_text = text
    
    def __str__(self):
        return self.origin_text
    
    
    
class JpText(Text):
    '''
    classdocs
    '''
    
    @staticmethod
    def get_text_by_dir(directory, filename):
        return Text._get_text_by_dir(directory, filename, lambda text : JpText(text))
    
    def __init__(self, text):
        '''
        Constructor
        :param text: テキスト
        '''
        super().__init__(text)
        
        self.mecab_trigger = MeCab.Tagger('mecabrc')
        self.mecab_result  = self.mecab_trigger.parse(text)
        
        self.words = self._get_words()
    
    def _get_words(self):
        words = []
        splited_words = self.mecab_result.split('\n')
        for splited_word in splited_words :
            if splited_word == 'EOS' or splited_word == '':
                break
            splited_word_info = splited_word.split(',')
            words.append(splited_word_info)
        return words
    
    def get_noun(self):
        noun_words = []
        for word in self.words:
            word_info = word[0].split('\t')
            if word_info[1] == '名詞' :
                noun_words.append(word_info[0])

        return noun_words
    
    def get_tf_idf(self, corpus):
        vectorizer = TfidfVectorizer(analyzer=Text._get_words, min_df=1, max_df=50)
        vectorizer.fit_transform(corpus)