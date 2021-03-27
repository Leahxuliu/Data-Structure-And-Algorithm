class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        if len(s) == 1:
            return 1

        def dfs(start, path):
            nonlocal res
            if start == N:
                res = max(res, len(path))
            
            for i in range(start, N):
                temp = s[start:i + 1]
                if s[start:i + 1] not in path:
                    #path.append(temp)
                    #dfs(i + 1, path)
                    #path.pop()

                    # 等同于
                    dfs(i + 1, path + [temp])

            return      

        res = 0
        N = len(s)
        dfs(0, [])
        return res
        