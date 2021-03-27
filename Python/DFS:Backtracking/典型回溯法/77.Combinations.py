# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/02  
# @Author  : XU Liu
# @FileName: 77.Combinations.py

'''
1. 题目类型：


2. 题目要求与理解：


3. 解题思路：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

'''
逻辑框架
k==2
k==3就再多一个for
'''
'''class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        res = []
        temp = []
        for i in range(1,n+1):
            temp.append(i)
            for j in range(i+1, n+1):
                temp.append(j)
                res.append(temp[:])  # ending
                temp.pop()
            temp.pop()
        return res'''

'''
写成回溯
上面的例子里面关键点就是
for i in range(1,n+1):
    temp.append(i)
    temp.pop()

第一层选择--第二层选择--返回第二层选择--返回第一层选择
'''
class Solution:
    def combine(self, n, k):
        res = []
        temp = []
        def backtrack(i, temp):
            if len(temp) == k:
                res.append(temp[:])
                return res  # 有没有这一行都行，但是有这一行会提前结束本循环
                
            for i in range(i,n+1):
                temp.append(i)
                backtrack(i+1, temp)
                temp.pop()
            return res
        
        backtrack(1, temp)
        return res

x = Solution()
print(x.combine(4,2))