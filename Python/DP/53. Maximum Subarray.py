'''
53. Maximum Subarray

连续最大subarray
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return sum(nums)
        
        # 注意初始化，不能是0要是float('-inf)
        sumVal = float('-inf')
        max_sum = float('-inf')

        for i in nums:
            if i > sumVal + i:
                sumVal = i 
            else:
                sumVal += i
            max_sum = max(max_sum, sumVal)
        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        res = nums[0]
        pre = nums[0]

        for i in range(1, len(nums)):
            pre = max(pre + nums[i], nums[i])
            res = max(res, pre)
        return res

'''
dp[i]: the max sum in nums[:i + 1] including nums[i]
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # corner case
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n 
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] =  max(dp[i - 1] + nums[i], nums[i])

        return max(dp)
