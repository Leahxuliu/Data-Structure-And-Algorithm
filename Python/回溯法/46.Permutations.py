# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/01  
# @Author  : XU Liu
# @FileName: 46.Permutations.py

'''
1. 题目类型：
    回溯法

2. 题目要求与理解：
    给定一个所有元素都不同的list，要求返回list元素的全排列

3. 解题思路：
    回溯

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        def backtracking(per):
            if len(per) == len(nums):
                res.append(per[:])
                return

            for i in nums:
                if i not in per:
                    per.append(i)
                    backtracking(per)
                    per.pop()
            
            return 
        
        res = []
        backtracking([])
        return res


# DFS
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        def DFS(per):
            if len(per) == len(nums):
                res.append(per[:])

            for i in nums:
                if i not in per:
                    per.append(i)
                    DFS(per[:])
            
            return 
        
        res = []
        DFS([])
        return res