'''
162

162. Find Peak Element
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return r