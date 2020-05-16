'''
Method - Two pointer
Steps:
    1. sort the nums
    2. traverse the number in nums, i
    3. set l == N + 1, r == len(nums) - 1
    4. if nums[i] + nums[l] + nums[r] == 0 --> append solution into res
       if nums[i] + nums[l] + nums[r] >  0 --> j -=1
       if nums[i] + nums[l] + nums[r] < 0  --> i += 1
       until i == j

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
         
        nums.sort()
        n = len(nums)
        res = set()  # 关键点
        for i in range(n):
            if nums[i] == nums[i-1] and i > 0:  # 去重，但是i>0
                continue
            l = i + 1
            r = n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
        return [list(x) for x in res]
        
        
        
        
        
        
        
        
        
        