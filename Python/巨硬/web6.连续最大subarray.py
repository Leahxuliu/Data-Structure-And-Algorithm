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