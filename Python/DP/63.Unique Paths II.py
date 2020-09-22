# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/14  
# @Author  : XU Liu
# @FileName: 62.Unique Paths.py

'''
1. 题目类型：
    DP 多少种路径

2. 题目要求与理解：
    m * n的网格
    从(0,0)点到(m-1,n-1)点有几种路径，每次移动只能向下或者向右\
    路上有障碍物，1表示障碍，0表示空位置

3. 解题思路：
    dp[i][j]:从起点到达i，j点有多少个路径
    状态转移方程：
        dp[i][j]  if 没有障碍
                 = dp[i-1][j] + dp[i][j-1]
    base case:
        dp[0][0] = 1  # 题目设定是 1
        dp[0][1] = 1
        dp[1][0] = 1

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
'''

'''
易错点！
注意起点和终点是障碍的情况！！！！

'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid == [[]] or obstacleGrid == []:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
    
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n -1] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                elif i == 0:
                    if obstacleGrid[0][j] == 0:
                        dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    if obstacleGrid[i][0] == 0:
                        dp[i][j] += dp[i - 1][j]
                else:
                    if obstacleGrid[i-1][j] == 0:
                        dp[i][j] += dp[i - 1][j]
                    if obstacleGrid[i][j-1] == 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n -1]