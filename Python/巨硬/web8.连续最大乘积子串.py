'''
152
有一个数组，从数组中找出连续数组乘积最大。
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) < 2:
            return nums[0]
        
        maxVal = nums[0]
        minVal = nums[0]
        res = nums[0]  # 易错
        

        for i in range(1, len(nums)):
            if nums[i] < 0:
                minVal, maxVal = maxVal, minVal

            maxVal = max(maxVal * nums[i], nums[i])
            minVal = min(minVal * nums[i], nums[i])
            res = max(res, maxVal)
        return res
