#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/27  
# @Author  : XU Liu
# @FileName: 374.Guess Number Higher or Lower.py

'''
1. 题目理解：
    猜数字，范围是1-n
    -1 : My number is lower  --> 猜的数比计算机的数要大
    1  : My number is higher
    0  : Congrats! You got it!


2. 题目类型：
    binary search

3. 输出输入以及边界条件：
input: int
output: int
corner case: 

4. 解题思路
    常规binary search
    后台有一个guess API

5. 时间空间复杂度：
    

'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            tag = guess(mid)
            
            if tag == 0:
                return mid
            elif tag == -1:
                r = mid - 1
            elif tag == 1:
                l = mid + 1
        