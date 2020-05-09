#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/07 

'''
I. Clarify
    no repeated integers

II. Method - Backtracking
    Steps:
        1. use all_res to store all possible subsets
        2. choose a integer from range(last time chose integer's index + 1, the number of nums + 1), add the integer into path
        3. add the path into all_res
        4. repeat step2 and step3 until no integer left
        5. pop
        (choose condition: range(last time chose integer's index + 1, the number of nums + 1))
        
    eg [1,2,3]
    
          []
        / | \
       1  2  3
      /\  |
     2  3 3
    /
   3
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        
        def backtracking(start, nums, path):
            all_res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i + 1, nums, path)
                path.pop()
        
        all_res = []
        backtracking(0, nums, [])
        return all_res