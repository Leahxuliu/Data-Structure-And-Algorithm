# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/02  
# @Author  : XU Liu
# @FileName: 78.Subsets.py

'''
1. 题目类型：


2. 题目要求与理解：
    找子集
    无重复树

3. 解题思路：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

'''
回溯法
易错点：
注意nums里的值与index，不要混淆
'''
class Solution:
    def subsets(self, nums):
        res = []
        temp = []
        
        def backtrack(index, temp):
            if temp not in res:
                res.append(temp[:])
                # return res 不能写return 因为的空list就会被append进去，没有进入到循环里面
            
            for i in range(index, len(nums)):
                temp.append(nums[i])
                backtrack(i + 1, temp)
                temp.pop()
            
            return res
        
        backtrack(0, temp)
        return res

x = Solution()
print(x.subsets([1,2,3]))

'''
写法2
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return 
        
        n = len(nums)
        all_res = []
        
        def backtrack(start, k, path):
            if len(path) == k:
                all_res.append(path[:])
            
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i+1, k, path)
                path.pop()
                
        for k in range(1, n + 1):
            backtrack(0, k, [])
            
        all_res.append([])
        return all_res


'''
优化
'''
'''
A. math idea 
数学归纳法
Time:O(2^n * n), product 2^n subset, add to res O(N)
Space:O(2^n * n)
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return 
        
        all_res = []
        
        def backtrack(start, path):
            all_res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
                
        backtrack(0, [])
        return all_res
        