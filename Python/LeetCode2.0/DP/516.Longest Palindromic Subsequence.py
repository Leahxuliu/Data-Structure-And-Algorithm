#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/09

'''
input: one word:str; the length of string is from 0 to inf;
output: int, (LSP)
corner case: the string is empty → 0

Method - DP (dp[i][j]: the number of LSP, when the words from i to j)
Steps:
    1. build dp table; the table size is n * n, n is the length of word; 
    2. scan table: i is from n-1 to 0, j is from i to n -1;  the result is dp[0][n-1]
        dp[i][j] = dp[i+1][j-1] + 2, when word[i] == word[j]
                  = max(dp[i + 1][j], dp[i][j -1]), when word[i] != word[j]
        base case:
            dp[i][j] = 1, i == j
Time Complexity: O(N**2)
Space Complexity: O(N**2)


'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
            