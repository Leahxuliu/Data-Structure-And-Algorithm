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
        
'''
dp[i]

initial value: False
dp[i] = dp[i - len(w)],  s[i-len(w):i] == w

0 1 2 3 4 5 6 7 8
- l e e t c o d e
T F F F T F F F T

'''


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == '':
            return False
        
        n = len(s)
        dp = [False] * (n + 1)
        
        for i in range(n + 1):
            if i == 0:
                dp[i] = True
            
            else:
                for w in wordDict:
                    if s[i - len(w):i] == w:
                        dp[i] = dp[i - len(w)]
                        if dp[i] == True:
                            break
        return dp[n]