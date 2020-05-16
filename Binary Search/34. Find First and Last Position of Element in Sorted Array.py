'''
Method - Binary Search
Steps:
    1. n: the number of nums
    2. set l start at 0, r start at n - 1, l <= r
    3. calculate mid = (l + r) // 2
    3. find first:
            if nums[mid] == target, r = mid - 1  # 易错
            if nums[mid] > target, r = mid - 1
            if nums[mid] < target, l = mid + 1
            return l
    4. find last:
            if nums[mid] == target, l = mid + 1
            if nums[mid] > target, r = mid - 1
            if nums[mid] < target, l = mid + 1
            return r
Time: O(logN)  2**times = N
Space: O(1)
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        if target < nums[0] or target > nums[-1]:  # 如果没有这个条件， [2,2]，8就会报错，因为l会out of range
            return [-1, -1]
        
        def firstPosition(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    r = mid - 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            # if 0 <= l < n and nums[l] == target:
            if nums[l] == target:
                return l
            else:
                return -1 
        
        
        def lastPosition(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            # if 0 <= r < n and nums[r] == target:
            if nums[r] == target:
                return r
            else:
                return -1 
                    
        res = []
        l, r = 0, n - 1
        res.append(firstPosition(l, r))
        res.append(lastPosition(l, r))
        return res
        
                