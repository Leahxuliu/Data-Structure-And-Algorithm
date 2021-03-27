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


'''
DP2

'''
def numDecodings(self, s: str) -> int:
    if s.startswith('0'):  # 开头有 ‘0’ 直接返回
        return 0

    n = len(s)
    dp = [1] * (n+1)  # 重点是 dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        if s[i-1] == '0' and s[i-2] not in '12':  # 出现前导 ‘0’ 的情况，不能解码，直接返回
            return 0
        if s[i-2:i] in ['10', '20']:  # 只有组合在一起才能解码
            dp[i] = dp[i-2]
        elif '10' < s[i-2:i] <= '26': # 两种解码方式
            dp[i] = dp[i-1] + dp[i-2]
        else:                         # '01'到 ‘09’ 或 > '26'，只有单独才能解码
            dp[i] = dp[i-1]
    return dp[n]


'''
dp
dp[i]: the number of ways when s[:i + 1]
dp[i] = dp[i - 1] + dp[i - 2]

01
10
001

1. 自己是0
		 能否与前一个数在一起
				前一个数是1或者是2，则可行 dp[i] = dp[i - 1]
				其它不可行 dp[i] = 0 !!!
		
2. 自己不是0
		 能否与前一个数在一起
				前一个数是0或者两数加在一起大于26，不可行 dp[i] = dp[i - 1]
				其它可行 dp[i] = dp[i - 1] + dp[i - 2]


'''

class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '':
            return 0
        if s[0] == '0':
            return 0
        
        
        n = len(s)
        dp = [0] * n 
        for i in range(n):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                if s[i] == '0':
                    if s[i - 1] == "1" or s[i - 1] == '2':
                        dp[i] = 1
                    else:
                        dp[i] = 0
                else:
                    if int(s[:2]) > 26 or s[i - 1] == "0":
                        dp[i] = 1
                    else:
                        dp[i] = 2
                
            else:
                if s[i] == '0':
                    if s[i - 1] == '1' or s[i - 1] == '2':
                        dp[i] = dp[i - 2]
                    else:
                        dp[i] = 0
                else:
                    if s[i - 1] == "0" or int(s[i - 1:i + 1]) > 26:
                        dp[i] = dp[i - 1]
                    else:
                        dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
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