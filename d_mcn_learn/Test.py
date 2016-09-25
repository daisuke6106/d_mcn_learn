'''
Created on 2016/09/24

@author: dk
'''

from d_mcn_learn.document.HtmlDocument import HtmlDocument 

if __name__ == '__main__':
    html_document = HtmlDocument('<html><head><title>タイトル</title></head><body>内容</body></html>')
    print(html_document.get_content("body")[0])
    