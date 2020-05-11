#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/11

'''
Methon - Binary Search
Steps:
    1. set left and right boundary as 1 and num//2
    2. calculate mid as (l + r) // 2, if mid * mid == num, return True
        if mid^2 < num, set left as mid
        else, set right as mid
    3. else, return False
    # use binary search to find a integer, which i * i == num → True, else False

Time complexity:O(logN)
Space complexity: O(1)

'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:  # 易错
            return True
        
        l = 1
        r = num // 2
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
        return False