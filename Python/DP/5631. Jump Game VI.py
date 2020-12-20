'''
回溯或者DFS
找到所有可能性
第五个case就超时
'''

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(i, steps, res):
            if i == len(nums) - 1:
                self.max_res = max(self.max_res, res)
                return 
            
            
            for each in steps:
                if i + each < len(nums):
                    res += nums[i + each]
                    helper(i + each, steps, res)
                    res -= nums[i + each]
                
            return
        
        steps = [i for i in range(1, k + 1)]
        self.max_res = 0
        helper(0, steps, nums[0])
        return self.max_res


'''
dp
超时
时间复杂度是nk
'''
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            for j in range(max(0, i - k), i):
                dp[i] = max(dp[i], dp[j] + nums[i]) 
        
        return dp[len(nums) - 1]


'''
DP + 滑动窗口(用队列实现)
'''


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        heap = []
        heappush(heap, (-nums[0], 0))
        
        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heappop(heap)

            val = -heap[0][0]
            dp[i] = nums[i] + val
            heappush(heap, (-dp[i], i))
        return dp[-1]