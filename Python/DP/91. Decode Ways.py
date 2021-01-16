'''
DP

dp[i]
加一个字母 -> dp[i](加入的字母，以单个形式加入) + xxx(加入的字母与前一位组成两位数)

123
1， 2， 3
12， 3
1， 23

120
1， 20

dp[0][i]: 结尾是单个
dp[1][i]: 结尾是双

if s[i] != 0:
    dp[0][i] = dp[0]][i - 1] + dp[1][i - 1]
if int(s[i - 1] + s[i]) <= 26:
    dp[1][i] = dp[0][i - 1] 

dp[0][0] = 1
dp[1][0] = 0


'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '' or int(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        dp = [[0] * len(s) for _ in range(2)]
        if int(s[0]) != 0:
            dp[0][0] = 1
            dp[1][0] = 0

        for i in range(1, len(s)):
            if int(s[i]) != 0:
                dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
            
            if int(s[i - 1] + s[i]) <= 26:
                dp[1][i] = dp[0][i - 1]
        return dp[0][-1] + dp[1][-1]