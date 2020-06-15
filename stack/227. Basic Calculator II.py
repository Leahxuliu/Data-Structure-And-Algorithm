# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/15

class Solution:
    def calculate(self, s: str) -> int:
        flag = '+'
        stack = []
        nums = 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                nums = nums * 10 + int(s[i])
            
            if s[i] in '+-*/' or i == len(s) - 1:
                if flag == '+':
                    stack.append(nums)
                elif flag == '-':
                    stack.append(-nums)
                elif flag == '/':
                    #stack.append(stack.pop() // nums)  #  错误 -3 // 2 = -2；而题目需要等于-1
                    stack.append(int(stack.pop() / nums))
                elif flag == '*':
                    stack.append(stack.pop() * nums)
                nums = 0
                flag = s[i]
        print(stack)
        return sum(stack)