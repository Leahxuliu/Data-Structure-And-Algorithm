# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/16  
# @Author  : XU Liu
# @FileName: 11.Container With Most Water.py

'''
方法一 暴力解法
S(i,j)=min(h[i],h[j])×(j−i)
枚举所有可能性
时间复杂度： O(N**2)
Time Limit Exceeded 
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_res = 0
        n = len(height)
        
        for i in range(n - 1):
            for j in range(i+1, n):
                S = min(height[i], height[j]) * (j - i)
                max_res = max(max_res, S)
        return max_res


'''
对撞指针
左右两端向中间走
每一次都对比最大面积
l,r 短的那一边往里走
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_res = float('-inf')
        
        while l < r:
            S = min(height[l], height[r]) * (r - l)
            max_res = max(max_res, S)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_res