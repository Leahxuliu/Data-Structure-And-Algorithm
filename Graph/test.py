class Solution:
    def twoSum(self, nums):
        if nums is None:
            return None

        l, r = 0, len(nums) - 1
        while l < r :
            mid = l + (r - l) // 2
            if nums[mid] <= nums[mid + 1]:
                l = mid + 1  # 峰值肯定不是mid
            if nums[mid] > nums[mid + 1]:
                r = mid  # 峰值可能是mid
        
        return l

x = Solution()
print(x.twoSum([4,5,6,7,2,1]))           