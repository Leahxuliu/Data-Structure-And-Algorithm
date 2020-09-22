#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/07 

'''
I. Clarify

II. Method - Backtracking
    Steps:
        1. sort the nums
        
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        def backtrack(start, nums, path):
            if path not in all_res:
                all_res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, nums, path)
                path.pop()
        
        nums.sort()
        all_res = []
        backtrack(0, nums, [])
        return all_res