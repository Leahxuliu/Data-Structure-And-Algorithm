'''
dp: (n + 1) * (m + 1)
dp[i][j]: s[:j]与p[:i]是否是匹配的
初始都是False

if s[j - 1] == p[i - 1] or p[i - 1] == '.':
    dp[i][j] = dp[i - 1][j - 1] 
elif p[i - 1] == '*':
    if p[i - 2] == s[j - 1] or p[i - 2] == '.': 
        dp[i][j] = dp[i - 2][j] or dp[i - 2][j - 1] or dp[i][j - 1]  # 核心
    else:
        dp[i][j] = dp[i - 2][j]


base case
dp[0][0] = True
dp[0][j] = False
dp[i][0] = dp[i - 2][j] if p[i - 1] == '*' else False

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and p == '':
            return True
        # if s == '' or p == '':
        #     return False

        n = len(s)
        m = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            for j in range(n + 1):
                if j == 0:
                    if p[i - 1] == '*':
                        dp[i][j] = dp[i - 2][j]
                else:
                    if s[j - 1] == p[i - 1] or p[i - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[i - 1] == '*':
                        if p[i - 2] == s[j - 1] or p[i - 2] == '.': 
                            # single or multi
                            # dp[i][j] = dp[i][j - 1]
                            # empyt or single or multi
                            dp[i][j] = dp[i - 2][j] or dp[i - 2][j - 1] or dp[i][j - 1]  # 核心
                        
                         # no match
                         # 要放在后面 "ab" ".*"
                        else:
                            dp[i][j] = dp[i - 2][j]
                        

        # print(dp)
        return dp[-1][-1]