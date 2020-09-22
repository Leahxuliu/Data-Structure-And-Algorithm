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
    def permute(self, nums):
        res = []
        temp = []
        
        def backtrack(res, temp):
            if len(nums) == len(temp):
                res.append(temp[:])
                return res
            
            for i in nums:
                if i not in temp:
                    temp.append(i)
                    backtrack(res, temp)
                    temp.pop()
        
        backtrack(res, temp)
        return res

x = Solution()
print(x.permute([1,2,3]))