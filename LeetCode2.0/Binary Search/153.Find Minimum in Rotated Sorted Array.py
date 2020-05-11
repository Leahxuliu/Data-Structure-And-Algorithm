#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/11

'''
Method - Binary Search
Steps:
    1. set l as 0, r as the number of nums - 1
    2. calculate mid as (l + r) // 2, then compare mid value with left value
        if l < mid, it means left part is sorted, renew the minimum as left value and l = mid + 1
        if l == mid, renew the minimum as left value
        if l > mid, it means right part is sorted, renew the minimum as right value and r = mid - 1
    3. return minimum
        
        
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == []:
            return 
        
        l, r = 0, len(nums) - 1
        res = nums[0]
        
        while l <= r:
            mid = l + (r - l) //2
            if nums[l] < nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            elif nums[l] == nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            elif nums[l] > nums[mid]:
                res = min(res, nums[mid])
                r = mid - 1
        return res