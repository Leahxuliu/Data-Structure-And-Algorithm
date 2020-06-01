#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/31


# 从头开始扫nums和从尾开始扫nums
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]

        if target < nums[0] or target > nums[-1]:
            return [-1, -1]

        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] == target:
                res.append(i)
                break
        else:
            return [-1, -1]
        
        for j in range(n-1, -1, -1):
            if nums[j] == target:
                res.append(j)
                break
        
        return res

        
# 二分搜索
class Solution:
    def searchRange(self, nums, target):
        if not nums:  # corner case
            return [-1, -1]

        if target < nums[0] or target > nums[-1]:  # 一定要先判断这个，不然会out of the range
            return [-1, -1]
        
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        return [first, last]
        
    def findFirst(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid  = l + (r - l) // 2
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if nums[l] == target:
            return l
        else:
            return -1
                
    def findLast(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid  = l + (r - l) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if nums[r] == target:
            return r
        else:
            return -1