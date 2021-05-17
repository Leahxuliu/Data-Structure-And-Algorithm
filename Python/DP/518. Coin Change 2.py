'''
brout force

用start在回溯里面可以避免重复
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        def find(start, count):
            if count == amount:
                self.res += 1
                return
            
            for i in range(start, len(coins)):
                if count + coins[i] <= amount:
                    find(i, count + coins[i])
            return 
        
        self.res = 0
        coins.sort()
        find(0, 0)
        return self.res


'''
DFS + memo

错误会有很多重复的情况

比如：
8
[2,5,3]

[3,3,2] [2,3,3]
[3,5], [5,3]

也就是只能从0开始遍历到amount
不能从amout遍历到0
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        def find(start, count):
            if count in memo:
                return memo[count]

            # if count == 0:
            #     return 0
            # if count < coins[start]:
            #     return 0
            if count == 0:
                return 1

            res = 0
            for i in range(start, len(coins)):
                if count - coins[i] >= 0:
                    res += find(i, count - coins[i])

            memo[count] = res
            return res
        
        coins.sort()
        memo = {}

'''
要把start也作为变量放入memo的key中
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        def find(start, count):
            if (count, start) in memo:
                return memo[(count, start)]

            if count == 0:
                return 1

            res = 0
            for i in range(start, len(coins)):
                if count - coins[i] >= 0:
                    res += find(i, count - coins[i])

            memo[(count, start)] = res
            return res
        
        coins.sort()
        memo = {}
        find(0, amount)
        print(memo)
        return find(0, amount)


'''
选与不选

'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        def find(start, count):
            if (count, start) in memo:
                return memo[(count, start)]

            if count == 0:
                return 1
            if start == len(coins):
                return 0

            res = 0
            # choose
            if count - coins[start] >= 0:
                res += find(start, count - coins[start])
            # not choose
            res += find(start + 1, count)

            memo[(count, start)] = res
            return res
        
        coins.sort()
        memo = {}
        return find(0, amount)
'''
DP

322与518的不同是什么
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if coins == []:
            return 0
        
        coins.sort()
        if amount < coins[0]:
            return 0
        
        
        dp = [0] * (amount + 1)
        dp[0] = 1
        # for i in range(1, amount + 1):
        #     for j in coins:
        #         if i - j >= 0:
        #             dp[i] += dp[i - j]
        #         else:
        #             break
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        # print(dp)
        return dp[-1]