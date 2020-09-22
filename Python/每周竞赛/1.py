class Solution:
    def maxScore(self, s: str):
        l = ''
        r = ''
        res = 0
        for i in range(1, len(s)):
            l = s[:i]
            print(l)
            r = s[i:]
            res = max(res, l.count('0') + r.count('1'))
        return res

X = Solution()
print(X.maxScore('1111'))