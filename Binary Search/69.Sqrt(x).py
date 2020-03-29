#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/29  
# @Author  : XU Liu
# @FileName: 69.Sqrt(x).py

'''
1. 题目类型：
    binary search

2. 题目理解以及解题思路：
    求平方根
    4 --> 2
    8 --> 2 因为2*2<8<3*3,也就是l,r互换跳出循环时的r
    先对半砍，再binary search，注意1，2

3. 输出输入以及边界条件：
input: int
output: int
corner case: 1


4. 时间空间复杂度：
    space：O(1)
    time:O(logN)

'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l, r = 0, x//2  # 易错，不要-1
        while l <= r:
            mid = l + (r - l)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
        return r
            


'''
Pocket Calculator Algorithm
x = e^logx -> x^1/2 = e^(1/2 * logx)
'''
from math import e, log


class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1
        return left if right * right > x else right