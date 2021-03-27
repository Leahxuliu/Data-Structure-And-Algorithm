'''
类似95 + memo

'''

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        
        def bulid(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            if start > end:
                return 1
            
            if start == end:
                return 1
            
            res = 0
            for i in range(start, end + 1):
                l = bulid(start, i - 1)
                r = bulid(i + 1, end)

                res +=  l * r 
            memo[(start, end)] = res
            return res 
        
        memo = {}
        return bulid(1, n)


class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        
        dp = [0] * (n + 1)
        # root = None
        dp[0] = 1
        # root.left == None and root.right == None
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                # left * right
                dp[i] += dp[j] * dp[i - j - 1]
        '''
        与递归保持一致
        for i in range(2, n + 1):
            for mid in range(i + 1):
                # left * right
                dp[i] += dp[mid - 1] * dp[i - mid]
        '''
        
        return dp[-1]