#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/20


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        new_S = []
        new_T = []
        for i in S:
            if i == '#':
                if new_S != []:
                    new_S.pop()
            else:
                new_S.append(i)
        
        for j in T:
            if j == '#':
                if new_T != []:
                    new_T.pop()
            else:
                new_T.append(j)

        if ''.join(new_S) == ''.join(new_T):
            return True
        else:
            return False
            

# 优化写法
class Solution:
    def backspaceCompare(self, S, T):
        def build(S):
            res = []
            for i in S:
                if i != '#':
                    res.append(i)
                elif res:
                    res.pop()
            return "".join(res)
        return build(S) == build(T)


