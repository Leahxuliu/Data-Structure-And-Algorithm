'''
原地hash
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while nums[i] - 1 != i:
                change_index = nums[i] - 1
                if nums[change_index] == nums[i]:
                    return nums[i]
                
                nums[i], nums[change_index] = nums[change_index], nums[i]
        return -1


'''
二分查找
1～N之间取中间值mid
遍历nums，数小于等于mid的数有多少个（count）
如果count > mid,也就是[1, mid]之间存在重复，right = mid
反之，left = mid + 1

时间复杂度：O（nlogn)
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        l = 1
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            
            if count > mid:
                r = mid
            else:
                l = mid + 1
        return l 
        