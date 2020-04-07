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


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    时间复杂度：O(n^2)
    空间复杂度：O(n^2)

'''

'''
dp + table
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


x = Solution()
print(x.longestPalindromeSubseq('cbbd'))

'''
dp+memo
好处：不用考虑遍历方向
'''


'''
递归
'''



'''
递归+memo
'''