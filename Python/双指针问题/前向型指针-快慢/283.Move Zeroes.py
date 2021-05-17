#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/28  
# @Author  : XU Liu
# @FileName: 283.Move Zeroes.py

'''
1. 题目要求：
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

2. 理解：


3. 输出输入以及边界条件：
input: nums: List[int]
output: nums: List[int]
corner case: None

4. 解题思路
two pointer fast slow
i, j = 0, 0
nums[j] == 0 --> j += 1
nums[j] != 0 --> nums[i] <-> nums[j] 互换
    
5. 空间时间复杂度

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        
        '''
        s是可放置的位置
        f找非0的值，要是遇到非0的值就放到s所指的地方
        '''
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1


'''
快慢双指针

   0, 1, 0, 3, 12
   s  f
   1  0  
      s  f  f
      3     0

s指向0
f指向s之后的非0 

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return 
        
        
        n = len(nums)
        s = 0
        f = 0

        # find first 0
        for i in range(n):
            if nums[i] == 0:
                s = i 
                break

        if nums[s] != 0 or s == n - 1:
            return 

        # find first non-zero after s
        # [1,0,1]所以一定要找到第一个s之后的
        for i in range(s + 1, n):
            if nums[i] != 0:
                f = i 
                break
        # like [1,0,0]
        if nums[f] == 0 or s >= f:
            return 

        while s < n and f < n:

            nums[s], nums[f] = nums[f], nums[s]
            while s < n and nums[s] != 0:
               s += 1

            while f < n and nums[f] == 0:
                f += 1
        return 
        

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return 
        
        s = 0
        f = 0
        n = len(nums)

        while f < n and s <= f:
            while s < n and nums[s] != 0:
                s += 1
                f = s

            while f < n and nums[f] == 0:
                f += 1

            if f < n and s <= f:
                nums[s], nums[f] = nums[f], nums[s]
                s += 1
                f += 1
            else:
                break
        return 