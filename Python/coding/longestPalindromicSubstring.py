'''
5. Longest Palindromic Substring
注意题目的return是什么
'''

def longestPalindrome(self, s: str) -> str:
    if s == '':
        return ''
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    max_len = 1
    start = 0
    
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = True
            
            elif j - i == 1:
                if s[i] == s[j]:
                    dp[i][j] = True
                    if max_len < 2:
                        max_len = 2
                        start = i
            else:
                if s[i] == s[j] and dp[i + 1][j - 1] == True:
                    dp[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        start = i
    return s[start:start + max_len]