#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/15

'''
Method - Binary Search
Steps:
    1. set l start at 0, r start at x//2; l <= r
    2. calculate mid = (l + r) //2, temp = mid * mid
    3. if temp == x, return ,mid
       if temp > x, r = mid - 1
       if temp < x, l = mid + 1
       return r
       
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        l, r = 0, x//2
        while l <= r:
            mid = l + (r - l) // 2
            temp = mid * mid
            if temp == x:
                return mid
            elif temp > x:
                r = mid - 1
            elif temp < x:
                l = mid + 1
        
        return r