'''

一维dp 
dp size: len(s) + 1
dp = [0] * len(s) + 1
dp[0] = 1
dp[1] = 1

s[0] == 0 --> return 0

travesal s[1:]
1. s[i - 1] is 0
		a. s[i - 2] is not 1 or 2 --> return 0
		b. dp[i] = dp[i - 2] !!!
2. s[i - 1] is not 0
		a. if 10 < s[i - 2:i] <= 26, dp[i] =dp[i - 1] + dp[i - 2]
		b. dp[i] = dp[i - 1]

'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "":
            return 0
        if s[0] == "0":
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] == "0":
                if s[i - 2] not in "12":
                    return 0
                else:
                    dp[i] = dp[i - 2]
            else:
                if 10 < int(s[i - 2:i]) <= 26:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]
        return dp[-1]