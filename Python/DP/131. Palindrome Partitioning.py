'''
backtracking
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # corner case
        if len(s) == 1:
            return [[s]]
        
        def check(start, end):
            '''
            if arr is palindrom, return True
            '''
            l = start
            r = end

            while l <= end and r >= 0 and l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtracking(start, part):
            '''
            find all combinations
            '''
            if start >= len(s):
                res.append(part[:])
                return

            for i in range(start, len(s)):
                # arr = s[start:i + 1] 时间复杂度高
                if check(start, i):
                    part.append(s[start: i + 1])
                    backtracking(i + 1, part)
                    part.pop()
            return 

        res = []
        backtracking(0, [])
        return res
        

'''
backtracking + DP
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # corner case
        if len(s) == 1:
            return [[s]]
        
        def check(s):
            '''
            make a dp table
            if arr is palindrom, return True
            '''
            n = len(s)
            dp = [[False] * n for _ in range(n)]
            for i in range(len(s) - 1, -1, -1):
                for j in range(i, len(s)):
                    if s[i] != s[j]:
                        dp[i][j] = False
                    else:
                        if i == j:
                            dp[i][j] = True
                        elif j - i == 1:
                            dp[i][j] = True
                        else:
                            dp[i][j] = dp[i + 1][j - 1]
            return dp

        def backtracking(start, part):
            '''
            find all combinations
            '''
            if start >= len(s):
                res.append(part[:])
                return

            for i in range(start, len(s)):
                # arr = s[start:i + 1] 时间复杂度高
                if dp[start][i]:
                    part.append(s[start: i + 1])
                    backtracking(i + 1, part)
                    part.pop()
            return 

        res = []
        dp = check(s)
        backtracking(0, [])
        return res
        
        



