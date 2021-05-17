# 贪心
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) < 2:
            return 0 
        
        i = 1
        res = 0
        while i < len(s):
            if s[i] == s[i - 1]:
                temp = cost[i - 1]
                maxVal = cost[i - 1]

                while i < len(s) and s[i] == s[i - 1]:
                    temp += cost[i]
                    maxVal = max(maxVal, cost[i])
                    i += 1
                
                res += temp - maxVal
            else:
                i += 1

        return res

# 双指针
# 有点难理解
# 左指针是用来表示这个字母没有被删除的index
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s) < 2:
            return 0

        n = len(s)
        i = 0
        res = 0

        
        for j in range(1, n):
            if s[i] == s[j]:
                if cost[j] > cost[i]:
                    res += cost[i]
                    i = j
                else:
                    res += cost[j]
            else:
                i = j 
        return res