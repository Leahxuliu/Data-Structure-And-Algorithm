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
        if nums == None:
            return 0
        
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j += 1
        return nums