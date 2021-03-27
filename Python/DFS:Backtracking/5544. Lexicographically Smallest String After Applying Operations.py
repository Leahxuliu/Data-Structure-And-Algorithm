class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        b = b % len(s)

        def addOption(s):
            chars = [c for c in s]
            for i in range(1, len(s), 2):
                chars[i] = str(int(chars[i]) + a)[-1]
            return ''.join(chars)

        def rotateOption(s):
            return s[-b:] + s[:-b]
        
        def dfs(s):
            if s in res:
                return 
            res.add(s)

            s1 = addOption(s)
            s2 = rotateOption(s)
            dfs(s1)
            dfs(s2)
        
        res = set()
        dfs(s)
        return min(res)