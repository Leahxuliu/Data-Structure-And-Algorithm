class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums == []:
            return -1
        l = 0
        r = len(nums) - 1
        res = float('inf')
        
        while l <= r:
            mid = l + (r - l) // 2
            res = min(res, nums[mid])
            
            if nums[l] < nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            elif nums[l] > nums[mid]:
                r = mid
            else:
                l += 1
        return res