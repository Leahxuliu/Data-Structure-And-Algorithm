#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/17

'''
Method - binary search
1. set l, r start at 0, the number of nums - 1, l <= r
2. do while loop
    1. calculate mid = (l + r) // 2
    2. compare nums[mid] and nums[l] and target and nums[r]

4. if can not find nums[mid] == target, return -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1