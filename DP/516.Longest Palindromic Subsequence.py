# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04  
# @Author  : XU Liu
# @FileName: 

'''
1. 题目类型：
    DP

2. 题目要求与理解：
    给定一个字符串 s，找到 s 中最长的回文子串。


3. 解题思路：
    dp[i][j] = dp[i+1][j-1] + 2, si == sj
    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]), si != sj

    base case
    dp[i][j] = 1 (i==j)  # 只有一个字符串
    i > j 初始化为0

    斜着遍历或者反着遍历
    return dp[0][n-1]

    # 如果str_a整个都是回文的话，比如len(str_a) = 5, 遍历过的点：[2,2]-->[1,3]-->[0,4]

'''



'''
递归
time  O(2**n)
Time Limit Exceeded
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == '':
            return 0
        
        def dfs(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                return dfs(i+1, j-1) + 2
            
            else:
                return max(dfs(i,j-1), dfs(i+1,j))
        
        return dfs(0, len(s) - 1)


'''
递归+memo
好处：不用考虑遍历方向,有的时候比dp也快
时间复杂度：O(N) 最好情况  O(N**2) 最坏情况
空间复杂度：O(N)
'''
class Solution2:
    def longestPalindromeSubseq2(self, s: str) -> int:
        if s == '':
            return 0
        
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                memo[(i,j)] = dfs(i+1, j-1) + 2
            else:
                memo[(i,j)] = max(dfs(i,j-1), dfs(i+1,j))
            return memo[(i, j)]

        return dfs(0, len(s) - 1)





'''
dp + table
时间复杂度：O(n^2)
空间复杂度：O(n^2)
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        if s == '':
            return 0
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                #print('i: ' + str(i) + '\t' + 'j: ' + str(j))
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][n-1]


x = Solution2()
print(x.longestPalindromeSubseq2('cbbdc'))





