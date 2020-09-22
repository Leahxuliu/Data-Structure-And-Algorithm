#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/17

'''
Method - Two pointers (fast and slow)
Steps:
    1. set i, j start at 0, 1
    2. if nums[i] == nums[j], j move (j += 1)
       if nums[i] != nums[j], i move one(i += 1), then nums[i] = nums[j], then j move
    3. when j move to the end, return i + 1

Time: O(N)
Space:O(1)
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        i, j = 0, 1
        while j <= len(nums) - 1:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1

        return i + 1