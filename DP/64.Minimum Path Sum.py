# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04  
# @Author  : XU Liu
# @FileName: 64.Minimum Path Sum.py

'''
1. 题目类型：


2. 题目要求与理解：
    最小路径和

3. 解题思路：
    dp[i][j]表示到达这个点的时候，最小路径
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    base：
    dp[0][0] = grid[0][0]
    dp[0][j] = dp[i][j-1] + grid[i][j]
    dp[i][0] = dp[i-1][j] + grid[i][j]

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == [] or grid == [[]]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[0][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
        