# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/15


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        flag = 1
        num = 0
        res = 0
        
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            
            elif i == '+':
                res += flag * num
                flag = 1
                num = 0
            elif i == '-':
                res += flag * num
                flag = -1
                num = 0
            elif i == '(':
                stack.append(res)
                stack.append(flag)
                flag = 1
                res = 0
            elif i == ')':
                res += flag * num
                num = 0
                flag = 1
                res = stack.pop() * res + stack.pop()
        res += flag * num
        return res