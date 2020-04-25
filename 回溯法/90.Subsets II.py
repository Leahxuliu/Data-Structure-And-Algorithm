# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/01  
# @Author  : XU Liu
# @FileName: 90.Subsets II.py

'''
1. 题目类型：


2. 题目要求与理解：
    找子集
    与78类似
    可以套用78的代码，但是
    input：[4,4,4,1,4]
    78题代码：[[],[4],[4,4],[4,4,4],[4,4,4,1],[4,4,4,1,4],[4,4,4,4],[4,4,1],[4,4,1,4],[4,1],[4,1,4],[1],[1,4]]
    正确答案：[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

3. 解题思路：
    nums.sort()


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

class Solution:
    def subsetsWithDup(self, nums):
        if nums == []:
            return 
        
        nums.sort()
        def backtrack(start, path):
            if path not in all_res:
                all_res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        all_res = []
        backtrack(0, [])
        return all_res


x = Solution()
print(x.subsetsWithDup([4,4,4,1,4]))


'''
错误
输出：[[],[1],[1,2],[1,2],[2],[2]]
正确：[[],[1],[1,2],[1,2,2],[2],[2,2]]
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return 
        def backtrack(start, path):
            all_res.append(path[:])
            
            for i in range(start, len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(i+1, path)
                    path.pop()

        all_res = []
        backtrack(0, [])
        return all_res