'''
Created on 2016/09/25

@author: dk
'''

import MeCab

from sklearn.feature_extraction.text import TfidfVectorizer

class Text(object):
    '''
    classdocs
    '''


    def __init__(self, text):
        '''
        Constructor
        '''
        self.origin_text = text
        
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