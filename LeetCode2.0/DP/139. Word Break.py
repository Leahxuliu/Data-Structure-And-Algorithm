# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/29

'''
dp[i]: s[0:i] 是否符合条件
if dp[j] == True and nums[j:i+1]in wordDict, True
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == '':
            return True
        
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        
        for i in range(n+1):
            each_word = ''
            for j in range(i-1, -1, -1):
                each_word = s[j] + each_word
                if dp[j] == True and each_word in wordDict:
                    dp[i] = True
                    break  # 易错
                else:
                    dp[i] = False
        return dp[n]
        