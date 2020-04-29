#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/29  
# @Author  : XU Liu
# @FileName: 350.Intersection of Two Arrays II.py

'''
1. 题目要求：


2. 理解：
与349类似
不同点：349输出的结果里面不能有重复，350是要有重复的，按实际有的次数输出
把set改成list就行了

3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == [] or nums2 == []:
            return 
        
        i, j = 0, 0
        res = []
        
        nums1.sort()
        nums2.sort()
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res