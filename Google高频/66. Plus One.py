# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/14

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        new_digit = []
        pre = 1
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + pre
            if temp >= 10:
                new_digit.insert(0, temp - 10)
                pre = 1
            else:
                new_digit.insert(0, temp)
                pre = 0
        if pre == 1:  # 易错
            new_digit.insert(0, pre)
        return new_digit