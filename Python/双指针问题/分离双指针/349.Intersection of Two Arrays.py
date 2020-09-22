#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/29  
# @Author  : XU Liu
# @FileName: 349.Intersection of Two Arrays.py

'''
1. 题目要求：
给定两个数组，编写一个函数来计算它们的交集。
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]

2. 理解：
找相同的值

3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
1. 对两个nums进行sort，从小到大排
2. 分离指针，每个nums里面一个指针，i，j，从0开始
3. 一样的值就放入到set里面
    
5. 空间时间复杂度
时间 O(N)
空间 O(1)
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 == [] or nums2 == []:
            return 
        
        i, j = 0, 0
        res = set()
        
        nums1.sort()
        nums2.sort()
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(res)