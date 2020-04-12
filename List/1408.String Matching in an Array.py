#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/12  
# @Author  : XU Liu
# @FileName: 1408.String Matching in an Array.py

'''
周赛
关键点： 

a = 'abcc'
c = 'ab'
if c in a:
    print('OK')

'''
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if words == []:
            return []
        
        res = []
        for w1 in words:
            for w2 in words:
                if w1 != w2:
                    if w1 in w2:
                        if w1 not in res:
                            res.append(w1)
        return res
