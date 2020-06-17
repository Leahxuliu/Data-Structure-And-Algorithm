#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/11

# 左右括号的个数，错误
# Input: "([)]" --> False
from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        
        info = defaultdict(int)
        for i in s:
            if i == '(':
                info[1] += 1
            elif i == ')':
                info[2] += 1
            elif i == '{':
                info[3] += 1
            elif i == '}':
                info[4] += 1
            elif i == '[':
                info[5] += 1
            elif i == ']':
                info[6] += 1
        
        if info[1] != info[2]:
            return False
        if info[3] != info[4]:
            return False
        if info[5] != info[6]:
            return False
        return True


# 用stack
# 左括号的存入stack
# 遇到右括号，stack.pop,pop出来的不是对应的左括号，则False

class Solution:
    def isValid(self, s: str) -> bool:
        if s == '':
            return True
        
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if not stack or stack.pop() != '(':  # 易错，一定要判断stack是不是空了
                    return False
            elif i == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif i == ']':
                if not stack or stack.pop() != '[':
                    return False

        if stack == []:  # 易错，最后stack里面可能还有剩余
            return True
        else:
            return False
            