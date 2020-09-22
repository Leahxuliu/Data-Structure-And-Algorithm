#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/29  
# @Author  : XU Liu
# @FileName: 153.Find Minimum in Rotated Sorted Array.py

'''
1. 题目类型：
    binary search

2. 题目理解以及解题思路：
    旋转过的arr，没有重复数(no duplicate exists in the array.)
    找到最小值
    存储一个temp的最小值
    比较num[l],num[mid],num[r]之间的关系

3. 输出输入以及边界条件：
input: nums: List[int]
output: int
corner case: none


4. 时间空间复杂度：
    

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == None:
            return 
        
        l, r = 0, len(nums)-1
        temp = nums[0]
        
        while l <= r:
            mid = l + (r - l)//2
            
            if nums[l] < nums[mid]:  # 左边是sorted，所以在l-mid之间，l最小
                temp = min(temp, nums[l])
                l = mid + 1
            elif nums[l] == nums[mid]:  # l到r之间久两个数，下一轮输出
                temp = min(temp, nums[l])  # 跟temp比较
                l = mid + 1
            elif nums[l] > nums[mid]:  # 右边是sorted，所以mid到r之间，mid最小
                temp = min(temp, nums[mid])
                r = mid - 1
                
        return temp