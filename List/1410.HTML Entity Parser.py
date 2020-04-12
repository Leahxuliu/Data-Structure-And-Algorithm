#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/12  
# @Author  : XU Liu
# @FileName: 1410.HTML Entity Parser.py

'''
关键点：
l.replace('','')
'''

class Solution:
    def entityParser(self, text: str) -> str:
        if text == '':
            return ''
        
        new_text = text.replace('&quot;', '"').replace("&apos;", "'").replace('&amp;', '&').replace('&gt;','>').replace('&lt;', '<').replace('&frasl;','/')
        
        return new_text