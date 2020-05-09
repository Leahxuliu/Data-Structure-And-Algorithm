#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/07

'''
I. Clarify
    all possible combinations of k numbers out of 1 ... n
    
    input: n:int, the value of n is from 1 to big enough; k:int, the value of k is from 0 to n
    output: List[list[int]]
    corner case: k == 0 return []

II. Method - backtracking
    Steps:
        1. use all_res to store all possible combinations
        2. choose a integer, add the integer into path
        3. if the length of path = k, the path will be added into all_res
        4. delete the integer
        5. repeat step2-step4
    Complexity:
        Time: O(k * CkN)
        Space:O(k * CkN)
    
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []
        def backtracking(i, n, k, path):
            if len(path) == k:
                all_res.append(path[:])
            
            for i in range(i, n+1):
                if i not in path:
                    path.append(i)
                    backtracking(i+1, n, k, path)
                    path.pop()
                    
        
        all_res = []
        backtracking(1, n, k, [])
        return all_res
        