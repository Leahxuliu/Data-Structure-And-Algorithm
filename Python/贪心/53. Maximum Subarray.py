# 贪心
# 错误
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        
        '''
        [-2, -1]
        按下面的逻辑最大就是-2了
        但正确是只取-1
        '''
        maxValue = max(prefix[1:])
        maxIndex = prefix.index(maxValue)
        minValue = min(prefix[:maxIndex])
        return maxValue - minValue

# 贪心
# 遍历prefix，prefix-右边最小的
# 时间复杂度 O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prefix = [nums[0]]
        for i in nums[1:]:
            prefix.append(prefix[-1] + i)
        
        res = float('-inf')
        minValue = 0
        for i in prefix:
            res = max(i - minValue, res)
            minValue = min(minValue, i)           
        
        return res

# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = nums
        for i in range(len(nums)):
            if i == 0:
                continue
            dp[i] = max(dp[i - 1] + nums[i], dp[i])
        
        return max(dp)

# 优化动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = nums[0]
        maxValue = nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue
            dp = max(dp + nums[i], nums[i])
            maxValue = max(dp, maxValue)
        
        return maxValue


# 分而治之
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def find(i):
            if i == 0:
                return nums[0]
            curr = max(nums[i], find(i - 1) + nums[i])
            self.res = max(self.res, curr)
            return curr
        
        self.res = nums[0]
        find(len(nums) - 1)
        return self.res

