#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/07
'''
I. Clarify
    to find all possible permutations
    
    input: nums:List[int]; the length of nums is from 0 to big enough; no repeated integers; 
    output: List[list[int]]
    corner case: nums is [] --> return []
    
II. Methode
    Backtracking 
    Steps:
        1. make a all_res(list) to store the possible permutations
        2. choose integer,then append interger into path
        3. when the length of path equal the length of nums, append this path into all_res
        4. deselect the integer
        5. repeat step2 - 4
    Complexity:
        Time: O(N * N!)  
        Space:O(N * N!) since one has to keep N! solutions.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        
        def backtracking(nums, path):
            if len(path) == len(nums):
                all_res.append(path[:])
                return 
            
            for i in nums:
                if i not in path:
                    path.append(i)
                    backtracking(nums, path)
                    path.pop()
            
        all_res = []
        backtracking(nums, [])
        return all_res