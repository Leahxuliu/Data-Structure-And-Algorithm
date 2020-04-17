# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/16  
# @Author  : XU Liu
# @FileName: 611.Valid Triangle Number.py

'''
1. 题目类型：


2. 题目要求与理解：
    给到的数组里面，任意三个数构成三角形
    能给构成三角形的个数有几个

    构成三角形的条件： 任意两条线段长度的和大于第三条线段的长度

3. 解题思路：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

'''
错误
不会
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        n = len(nums)
        nums.sort()
        res = 0
        
        for i in range(n):
            l = i + 1
            r = n - 1
            
            while l < r:
                if nums[i] + nums[l] > nums[r]:
                    res += 1
                    l += 1
                else:
                    r -= 1
        return res