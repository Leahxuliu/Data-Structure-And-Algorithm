#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/28  
# @Author  : XU Liu
# @FileName: 441.Arranging Coins.py

'''

1. 题目类型：
    binary search

2. 题目理解以及思路：
    给到的数，能否拆成1+2+3+4+5+...
    1+2+3+4....+ k = k(k+1)/2 = total
    k是层数，也是每一层的个数
    taget == total
    或者是在(k-1)层和与k层和之间 这种情况return k-1层，也就是r
    

3. 输出输入以及边界条件：
input: int
output: int
corner case: 1 

4. 时间空间复杂度：
    

'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            if mid * (mid + 1) //2 == n:
                return mid
            elif mid * (mid + 1) //2 > n:
                r = mid - 1
            elif mid * (mid + 1) //2 < n:
                l = mid + 1
        return r

