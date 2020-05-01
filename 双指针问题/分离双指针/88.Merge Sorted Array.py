#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/29  
# @Author  : XU Liu
# @FileName: 88.Merge Sorted Array.py

'''
1. 题目要求：
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
inplace
k = m + n -1
从nums1[k]开始往前放

    
5. 空间时间复杂度

'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while i >= 0 and j >= 0:
            print(nums1)
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            
        if j >= 0:
            nums1[:k + 1] = nums2[:j + 1]