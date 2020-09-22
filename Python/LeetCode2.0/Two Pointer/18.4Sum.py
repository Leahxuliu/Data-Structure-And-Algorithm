'''
Method - two pointers
Steps:
    1. sort nums
    2. n = len(nums)
    3. nums[i]: i is from 0 to n - 3
       nums[j]: j if from i+1 to n - 2
       set l start at j + 1, r start at n - 1
    4. calculate temp = nums[i] + nums[j] + nums[l] + nums[r]
       if temp == target, append them to res
       if temp > target, r -= 1
       if temp < target, l += 1
    
Time: O(N**3)
Space: O(1)
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n <= 3:
            return []
        
        res = set()
        nums.sort()
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                l, r = j + 1, n - 1
                
                while l < r:
                    temp = nums[i] + nums[j] + nums[l] + nums[r]
                    if temp == target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        r -= 1
                        l += 1
                    elif temp > target:
                        r -= 1
                    elif temp < target:
                        l += 1
        return [list(x) for x in res]