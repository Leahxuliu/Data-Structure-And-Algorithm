# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04  
# @Author  : XU Liu
# @FileName: 

'''
1. 题目类型：


2. 题目要求与理解：


3. 解题思路：
    dp[i][j]表示当前点为正方形的右下方的顶点时，正方形的最大面积
    if matrix[i][j] == 1:
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    if matrix[i][j] == 0:
        dp[i][j] = 0

    base:
    该点为1
    dp[0][0] = 1
    dp[0][j] = 1
    dp[i][0] = 1

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == [[]] or matrix == []:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = 1
                    elif j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
                    
        return res * res