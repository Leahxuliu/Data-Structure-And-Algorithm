'''
'cbbd'报错原因

这道题中的回文子串应该为**“bb”**但是我们的dp表中并没有计算出来，这是因为当计算dp[i][j]dp[i][j]的时候，中间已经没有dp[i+1][j-1]dp[i+1][j−1]了，这是我们在base case中没有考虑到的。由于我们在dp表中表示不出来，那我们就在计算的时候单独拿出来这种情况计算，即i和j相邻的时候:


'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return ''
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        max_len = 1
        start = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif i == j - 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        temp = j - i + 1
                        if temp > max_len:
                            start = i
                            max_len = temp
                else:
                    if s[i] == s[j] and dp[i+1][j-1] == True:
                        dp[i][j] = True
                        temp = j - i + 1
                        if temp > max_len:
                            start = i
                            max_len = temp

        return s[start: start + max_len]