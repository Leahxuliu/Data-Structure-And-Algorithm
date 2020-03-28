#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/28  
# @Author  : XU Liu
# @FileName: 35.Search Insert Position.py

'''
1. 题目理解：
    有target-->output index（0-based）
    没有target --> where it would be， eg [1,3,5,6], 2 --> 1

2. 题目类型：
    binary search

3. 输出输入以及边界条件：
input: nums: List[int], target: int
output: int
corner case:  

4. 解题思路
    use binary search
    有target--> return mid
    没有target --> l与r交换的地方，也就是本应该在的位置，return l 



5. 时间空间复杂度：
    

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return l