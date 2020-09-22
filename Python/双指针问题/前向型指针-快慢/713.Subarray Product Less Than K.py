#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/29  
# @Author  : XU Liu
# @FileName: 713.Subarray Product Less Than K.py

'''
1. 题目要求：
给定一个正整数数组 nums。
找出该数组内乘积小于 k 的连续的子数组的个数。

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路

1: 当 left <= right 且滑动窗口内的乘积小于 k 时，
    我们可以知道 [left,right]、[left+1,right]...[right-1,right] 均满足条件，
    因此，计数加 right-left+1，然后移动右边界（滑动区间加大），看剩下的区间是否满足乘积小于 k，
    如果小于 k，重复1，否则进行2。

2: 当滑动窗口内的乘积大于等于 k 时，右移左边界（滑动区间减小），如果这个区间内乘积小于 k，进入步骤 1，否则重复步骤 2。
    
5. 空间时间复杂度

'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if nums == []:
            return 0
        
        res = 0
        temp = 1
        l = 0
        
        for r in range(len(nums)):
            temp *= nums[r]
            
            while l <= r and temp >= k:
                temp /= nums[l]
                l += 1
            res += r - l + 1
        return res