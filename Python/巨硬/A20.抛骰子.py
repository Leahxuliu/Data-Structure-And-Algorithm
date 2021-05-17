'''
1155
抛骰子
'''
# DFS + memo
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # corner case
        if d * f < target:
            return 0

        def find(d, target):
            if (d, target) in memo:
                return memo[(d, target)]
            if d == 0 and target == 0:
                return 1
            if d < 0 or target < 0:
                return 0
            
            res = 0
            for i in range(1, f + 1):
                res += find(d - 1, target - i)

            memo[(d, target)] = res 
            return res

        memo = {}
        return find(d, target) % (10 ** 9 + 7)

# DP

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # corner case
        if d * f < target:
            return 0

        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1

        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for z in range(1, f + 1):
                    if j - z >= 0:
                        dp[i][j] += dp[i - 1][j - z]
                    else:
                        break
        return dp[-1][-1] % (10 ** 9 + 7)