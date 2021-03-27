'''
dp 
size:(i + 1) *  (j + 1)
dp[i][j]: whether s3[:i + j] is formed by s1[:i] and s2[:j]; bool

类似二维数组的路径问题,移动方向仅限于左和下

if s3[i + j - 1] = s1[i]
    dp[i][j] = dp[i - 1][j]
if s3[i + j - 1] = s1[i]
    dp[i][j] = dp2[i][j - 1]  

base case
dp[0][0] = True
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # corner cass
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == '' and s2 == '' and s3 == '':
            return True
        if s1 == '' and s2 == s3:
            return True
        if s2 == '' and s1 == s3:
            return True

        n = len(s1)
        m = len(s2)        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[0][0] = True
                elif i == 0:
                    if s3[i + j - 1] == s2[j - 1]:
                        dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    if s3[i + j - 1] == s1[i - 1]:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if s3[i + j - 1] == s1[i - 1] and dp[i - 1][j] == True:
                        dp[i][j] = True
                        continue
                    if s3[i + j - 1] == s2[j - 1] and dp[i][j - 1] == True:
                        dp[i][j] = True
                        continue
        return dp[-1][-1]
        
