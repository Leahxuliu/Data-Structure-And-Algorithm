# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/14

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if input == '':
            return ''
        
        input_arr = input.split('\n')
        
        res = 0
        path = []
        
        for i in input_arr:
            level = i.count('\t')
            i = i[level:]  # \t 算一个字符
            
            while level < len(path):  # key
                path.pop()
            
            if '.' in i:
                path.append(i)
                cur = len('/'.join(path))
                res = max(res, cur)
            else:
                path.append(i)
        return res