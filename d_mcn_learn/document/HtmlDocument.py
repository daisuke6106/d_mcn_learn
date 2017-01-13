'''
Created on 2016/09/22

@author: dk
'''
# -*- coding: utf-8 -*-

import glob

from d_mcn_learn.document.Text import Text
from bs4 import BeautifulSoup

class HtmlDocument(object):
    
    @staticmethod
    def get_html_by_dir(path):
        u"""
        引数に指定されたパスからHtmlファイルを元に複数のHtmlDocumentを生成し、返却します。
        :return htmlList: HtmlDocumentデータリスト
        """
        files = glob.glob(path)
        list  = []
        for file in files:
            list.append(HtmlDocument(open(file).read()))
            
        return list
        
    def __init__(self, data):
        u"""
        Constructor
        指定のHtml本文のデータを基にHtmlDocumentのインスタンスを生成します。
        :param data: Htmlデータ
        """
        self.data = data
        self.bs = BeautifulSoup(data)
    
    def get_title(self):
        u"""
        このHtmlDocumentのtitleタグに指定されている内容を取得します。
        :return title: このHtmlデータのタイトル文字列（文字列）
        """
        return Text( self.bs.find('title').text )
    
    def get_body_content(self):
        u"""
        このHtmlDocumentのbodyタグに指定されている内容を取得します。
        :return title: このHtmlデータのbody部の内容（文字列）
        """
        return Text( self.bs.find('body').text )
    
    def get_content(self, selector):
        u"""
        このHtmlDocumentから引数に指定されたcssセレクタを使ったタグを取得し、その内容を返却します。
        :return title: このHtmlデータのbody部の内容（文字列）
        """
        result_text = []
        element_list = self.bs.select(selector)
        for element in element_list:
            result_text.append( Text( element.text ) )
        return result_text