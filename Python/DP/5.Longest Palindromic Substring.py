'''
给你一个字符串 s，找到 s 中最长的回文子串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
'''

def longestPalindrome(s):
    if s == "":
        return ""
    
    n = len(s)
    dp = [[False] * (n) for _ in range(n)]
    start = 0
    maxLen = 1

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = True
            
            elif i + 1 == j:
                if s[i] == s[j]:
                    dp[i][j] = True
                    if j - i + 1 > maxLen:
                        start = i 
                        maxLen = j - i + 1
            else:
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] == True and j - i + 1 > maxLen:
                        start = i 
                        maxLen = j - i + 1

    return s[start:start + maxLen]