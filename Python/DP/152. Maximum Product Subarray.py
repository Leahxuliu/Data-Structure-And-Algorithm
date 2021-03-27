'''
brout force 
find all subarray 
O(n**2)

subarray里面一定要有偶数个负或者没有负数

res = 2, 6
product = 2, 6, 3
[2,  3,  -2,  4,  -1]
 l.  l    l
 r

'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # def DFS(start, product):
        #     '''
        #     find all subarray
        #     product: [subarray start, subarray end]
        #     '''
        #     if start >= len(nums):
        #         return 

        #     self.res = max(self.res, product)
        #     for i in range(start, len(s)):

        prefix = [1]
        for i in nums:
            if prefix[-1] == 0:
                prefix.append(i)
            else:
                prefix.append(prefix[-1] * i)

        self.res = nums[0]
        # backtracking(0, [])

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    self.res = max(self.res, 0)
                    break
                if prefix[i] == 0:
                    self.res = max(self.res, prefix[j + 1])
                    continue
                
                product = prefix[j + 1] / prefix[i]
                self.res = max(self.res, product)

        return int(self.res)

'''
dp

dp[i][0] the max value in nums[:i + 1]
dp[i][1] the min value in nums[:i + 1]
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        res = nums[0]
        imax = nums[0]
        imin = nums[0]

        for i in nums[1:]:
            if i < 0:
                imax, imin = imin, imax
                
            imax = max(imax * i, i)
            imin = min(imin * i, i)
            res = max(res, imax)
        return res