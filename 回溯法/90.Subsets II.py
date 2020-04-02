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
        res = []
        temp = []
        #nums.sort()  # 关键点
        def backtrack(index, temp):
            if temp not in res:
                res.append(temp[:])
            
            for i in range(index, len(nums)):
                temp.append(nums[i])
                #temp.sort()  # 错误，因为1被调到前面，pop的时候不能被删除
                backtrack(i + 1, temp)
                temp.pop()
            
            return res
        
        backtrack(0, temp)
        return res


x = Solution()
print(x.subsetsWithDup([4,4,4,1,4]))