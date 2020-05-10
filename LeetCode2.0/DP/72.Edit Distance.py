#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/09



'''
input: two words: str; the length of word is from 0 to inf
output: int; the number of modify steps
corner case: 
	one of the word is ‘’ → len(word2)
	both words are ‘’ → 0

Method - DP
Steps:
build DP table; the size of table is (len(word1) + 1)* (len(word2) + 1)
    dp[i][j]: the optimal solution when the size of word1 is i, the size of word2 is j
    dp[i][j] = dp[i-1][j-1], word1[i - 1] != word2[j - 1]
               = min(dp[i][j-1], dp[i-1][j],dp[i-1][j-1]) + 1, word1[i - 1] == word2[j - 1]
    result is dp[len(word2)][len(word1)]
base case:
	dp[0][j] = j
	dp[i][0] = i
    
Time Complexity: O(NM), N is the length of word1 and M is the length of word2
Space Complexity: O(NM), DP table’s size


'''

# 易错点，注意哪个word是行，哪个word是列; word1[i - 1] != word2[j - 1], 减1不能忘
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if m == 0:
            return n
        if n == 0:
            return m
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[n][m]