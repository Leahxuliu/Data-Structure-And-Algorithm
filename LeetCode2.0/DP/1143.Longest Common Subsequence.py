'''
Method - DP
dp[i][j]: the number of LCS, when compare text1[0:i] with text2[0:j]

Steps:
    1. build dp table, the table size is (len(text2) + 1) * (len(text1) + 1) [n * m]
    2. scan table from 1 to  m/n
    3. dp[i][j] = dp[i-1][j-1] + 1, text1[i -1] == text[j -1]
              = max(dp[i-1][j], dp[i][j-1]), text1[i-1] != text[j - 1]
        base case:
            dp[0][j] = 0
            dp[i][0] = 0

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        if m == 0 or n == 0:
            return 0
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]