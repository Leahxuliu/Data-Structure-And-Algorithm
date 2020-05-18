#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/18

'''
Method - DP
DP[i][j]: the min sum of [0][0] to [i][j]

Steps:
    1. build dp table, the size of table is m *n, initial value of dp[i][i] is 0 (float('inf') 也可)
    2. scan dp table, left to right, up to down
    3. dp[i][j] = min(from left + from up) + grid[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
       base case:
            dp[0][0] = grid[0][0]
            dp[i][0] = dp[i - 1][0] + grid[i][j]
            dp[0][j] = dp[0][j - 1] + grid[i][j]
    4. return dp[m - 1][n - 1]

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
                    dp[0][0] = grid[0][0]
                elif j == 0:
                    dp[i][0] = dp[i - 1][0] + grid[i][j]
                elif i == 0:
                    dp[0][j] = dp[0][j - 1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        print(dp)
        return dp[m - 1][n - 1]