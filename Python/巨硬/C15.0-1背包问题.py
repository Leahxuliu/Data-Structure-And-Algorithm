'''
416. Partition Equal Subset Sum
把一串数组分成两等分
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False 
        
        targe = sum_nums // 2
        dp = [False] * (targe + 1)
        dp[0] = True

        for i in range(len(nums)):
            pre = dp[:]
            for j in range(targe + 1):
                if pre[j] == True and j + nums[i] <= targe:
                    dp[j + nums[i]] = True
        return dp[-1]


'''
1155. Number of Dice Rolls With Target Sum
'''

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target:  # 勿忘！ 可以节约好多时间
            return 0

        if d == 0 or target == 0:
            return 0
        
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1

        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for each in range(1, f + 1):
                    if j - each < 0:
                        break
                    dp[i][j] += dp[i - 1][j - each]
        print(dp)
        return dp[-1][-1] % (10 ** 9 + 7)




'''
DFS + memo
'''

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0 or target == 0:
            return 0
        
        def find(d, target):
            if (d, target) in memo:
                return memo[(d, target)]

            if d == 0 and target == 0:
                return 0
            if d == 1 and 0 < target <= f:
                return 1
            if d < 0 or target < 0:
                return 0

            res = 0
            for each in range(1, f + 1):
                if target - each < 0:
                    break
                res += find(d - 1, target - each)
            memo[(d, target)] = res
            return res
        
        memo = {}  
        return find(d, target) % (10 ** 9 + 7)