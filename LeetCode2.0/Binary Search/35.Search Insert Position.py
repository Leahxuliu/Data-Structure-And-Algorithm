#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/13

'''
Method - Binary Search
Steps:
    1. set l as 0, r as len(nums) - 1
    2. calculate mid as (r - l) //2
    3. compare nums[mid] with target (l <= r)
        if nums[mid] == target, return mid
        if nums[mid] < target, l += 1
        if nums[mid] > target, r -= 1
    4. if can not find target in nums, return l

Time complexity: O(logN)  
Space: O(1)
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r -= 1
            elif nums[mid] < target:
                l += 1
        return l