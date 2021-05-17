'''
153
在旋转的sorted list里面找最小值
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        l = 0
        r = len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            # left is sorted
            if nums[l] < nums[mid]:
                res = min(nums[l], res)
                l = mid + 1
            
            # right is sorted
            elif nums[l] > nums[mid]:
                res = min(nums[mid], res)
                r = mid - 1

            else:
                res = min(nums[l], res)
                l = mid + 1

        return res