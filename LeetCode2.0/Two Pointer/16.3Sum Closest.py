'''
Method - two pointer
Steps:
    1. sort nums
    2. scan the nums from nums (nums[i])
    3. set l start at i + 1, r start at the end
    4. calculate temp = nums[i] + nums[l] + nums[r]
       if temp > target, r -= 1
       if temp < target, l += 1
       if abs(target - temp) < abs(target - res), renew the res

Time: O(nlogn + n*n) = O(n**2) sort + scan * scan
Space:O(1)


'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 
        
        nums.sort()
        n = len(nums)
        
        res = float('inf')
        for i in range(n - 2):
            l, r = i + 1, n - 1
            
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp > target:
                    r -= 1
                else:
                    l += 1
                
                if abs(target - temp) < abs(target - res):
                    res = temp
        return res