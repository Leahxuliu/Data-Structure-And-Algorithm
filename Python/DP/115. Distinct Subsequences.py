
'''
brout force
backtracking
find all subseq from s
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s == '' or t == '':
            return 0
        
        def findSubseq(start, path):
            if len(path) == len(t):
                if ''.join(path) == t:
                    self.res += 1
                return
            # 一定要放在上一个条件之后，因为start到最后的时候，有可能是答案
            # babgbag 取最后一个g
            if start >= len(s):
                return 

            for i in range(start, len(s)):
                if s[i] == t[len(path)]:
                    path.append(s[i])
                    findSubseq(i + 1, path)
                    path.pop()
            return
        
        self.res = 0
        findSubseq(0, [])
        return self.res



'''
brout force
backtracking
find all subseq from s


+ dict

'''
from collections import defaultdict
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s == '' or t == '':
            return 0
        
        def findSubseq(start, path):
            if len(path) == len(t):
                if ''.join(path) == t:
                    self.res += 1
                return
            # 一定要放在上一个条件之后，因为start到最后的时候，有可能是答案
            # babgbag 取最后一个g
            if start >= len(s):
                return 

            for i in info[t[len(path)]]:
                if i >= start:
                    path.append(s[i])
                    findSubseq(i + 1, path)
                    path.pop()
            return
        
        info = defaultdict(list)
        for i, each in enumerate(s):
            info[each].append(i)

        self.res = 0
        findSubseq(0, [])
        return self.res




'''
dp

dp[i][j]
s[:j + 1], t[:i + 1]的时候，有dp[i][j]种

  r a b b b i t
r
a
b
b
i
t

base case
i > j: dp[i][j] = 0
if s[0] == t[0], dp[i][j] = 1, else dp[i][j] = 0

if t[i] == s[j]:
    dp[i][j] = 选s[j]的情况 + 不选s[j]的情况 = dp[i - 1][j - 1] + dp[i][j - 1]
if t[i] != s[j]:
    dp[i][j] = 不选s[j]的情况 = dp[i][j - 1]

'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s == '' or t == '':
            return 0
        
        dp = [[0] * len(s) for _ in range(len(t))]
        for i in range(len(t)):
            for j in range(i, len(s)):
                if i == 0 and j == 0:
                    if t[i] == s[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                
                elif i == 0:
                    if t[i] == s[j]:
                        dp[i][j] = dp[i][j - 1] + 1
                    else:
                        dp[i][j] = dp[i][j - 1]
                
                else:
                    if t[i] != s[j]:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
        return dp[-1][-1]