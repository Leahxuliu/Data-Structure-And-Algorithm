'''
713
乘积小于K的子数组
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if nums == []:
            return 0
        if len(nums) == 1 and nums[0] < k:
            return 1
        

        res = 0
        left = 0
        count = 1
        for right in range(len(nums)):
            count *= nums[right]

            while count >= k:
                count //= nums[left]
                left += 1

            res += right - left + 1
        # res += right - left + 1
        return res