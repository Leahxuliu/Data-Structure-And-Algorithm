# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/07  
# @Author  : XU Liu
# @FileName: 72.Edit Distance.py

'''
1. 题目类型：
    dp

2. 题目要求与理解：
    编辑距离问题
    两个字符串 s1 和 s2，只能用增、删、替换，把 s1 变成 s2，求最少的操作数。

3. 解题思路：
    C[i,j]: S1[1..i]和S2[1..j]的编辑方程   
    C[i,j] = min{C[i-1,j]+1, C[i,j-1]+1, C[i-1,j-1]+1}，si != sj   
           = C[i-1,j-1]，si == sj   
    C[0,j] = j,   
    C[i,0] = i 

    dp(i, j - 1) + 1,    # 插入 (矩阵里面的右邻居)
    dp(i - 1, j) + 1,    # 删除 (矩阵里面的上邻居)
    dp(i - 1, j - 1) + 1 # 替换 (矩阵里面的斜邻居)

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    时间复杂度O(mn)

'''

class Solution:
    def minDistance(self, word1, word2):
        if word1 == word2:  # corner case
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        m = len(word1)
        n = len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[m][n]

