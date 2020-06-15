# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/15

'''
每次遇到操作符，从栈中pop 头两个数字；每次遇到数字，直接进栈。 
1. loop the tokens
2. if element is diget, add into stack
3. if element is + - * /
    a. pop 2 elements from stack, e1 and e2
    b. e2 + - * / e1 --> temp
    c put temp into stack
4. repeat step1 to step3
5. after traverse the tokens, return stack[0]

time: O(n)
space: best O(1) worst o(N/2)

'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        data = []
        for i in tokens:
            if i == '+':
                e1 = data.pop()
                e2 = data.pop()
                temp = e1 + e2
                data.append(int(temp))
            elif i == '-':
                e1 = data.pop()
                e2 = data.pop()
                temp = e2 - e1
                data.append(int(temp))
            elif i == '*':
                e1 = data.pop()
                e2 = data.pop()
                temp = e2 * e1
                data.append(int(temp))
            elif i == '/':
                e1 = data.pop()
                e2 = data.pop()
                temp = e2 / e1
                data.append(int(temp))
            else:
                data.append(int(i))
        return data[0]