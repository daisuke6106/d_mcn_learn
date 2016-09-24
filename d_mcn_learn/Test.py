'''
Created on 2016/09/24

@author: dk
'''

from d_mcn_learn.document.Text import Text 

if __name__ == '__main__':
    text = Text('テスト用文字列')
    noun_words = text.get_noun()
    print(noun_words)
    