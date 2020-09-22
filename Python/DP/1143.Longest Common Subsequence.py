# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/06  
# @Author  : XU Liu
# @FileName: 1143.Longest Common Subsequence.py

'''
1. 题目类型：
    DP

2. 题目要求与理解：
    找longest common subsequence

3. 解题思路：
    m = len(text1)
    n = len(text2)
    dp: （m+1） * （n+1）
    xi: text1
    yj: text2

    状态转移方程：
    if xi == yj:
        dp[i][j] = dp[i-1][j-1] + 1
    if xi != yj:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    易错点：
    dp是（m+1） * （n+1），有0行0列

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    space: O(n**2)

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        m = len(text1)  # len的计算时间复杂度是O(n)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]  # 易错

        for i in range(1, m+1):  # 注意范围
            for j in range(1, n+1):  # 注意范围
                if text1[i-1] == text2[j-1]:  # 易错
                    dp[i][j] = dp[i-1][j-1] + 1
                elif text1[i-1] != text2[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
