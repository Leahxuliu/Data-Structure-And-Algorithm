'''
brout force
backtracking
'''

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if arr == []:
            return 0
        
        def find(start, path):
            if start == len(arr):
                self.res = max(self.res, len(path))
            
            for i in range(start, len(arr)):
                # not choose
                find(start + 1, path)

                # choose
                if len(path) < 2 or (len(path) >= 2 and (path[-2] + path[-1] == arr[i])):
                    find(start + 1, path + [arr[i]])

            return 
        
        self.res = 0
        find(0, [])
        return self.res


'''
DP

dp[i] 表示从0到i，且包括arr[i]时的最长子序列
用longest来保存[m,n]从m开始到n的最长子序列，包括m和n

'''

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if arr == []:
            return 0
        
        info = {}
        for i in range(len(arr)):
            info[arr[i]] = i

        longest = {(0, 1): 2}

        dp = [0] * len(arr)
        dp[0] = 1
        dp[1] = 2

        for i in range(len(arr)):
            for j in range(i):
                diff = arr[i] - arr[j]
                if diff in info and info[diff] < j:
                    k = info[diff]
                    if (k, j) in longest:
                        longest[(j, i)] = longest[(k, j)] + 1
                    else:
                        longest[(j, i)] = 2 + 1
                    dp[i] = max(dp[i], longest[(j, i)])
        
        res = max(dp)
        return res if res >= 3 else 0
                
