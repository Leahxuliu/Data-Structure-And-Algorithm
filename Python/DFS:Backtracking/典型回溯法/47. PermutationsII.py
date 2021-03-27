class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums  == []:
            return []
        
        def backtacking(visited, per):
            if len(per) == len(nums):
                res.append(per[:])
                return
            
            for i in range(len(nums)):
                if visited[i] == 0:
                    if i > 0 and nums[i - 1] == nums[i] and visited[i - 1] == 1:
                        continue

                    visited[i] = 1
                    per.append(nums[i])
                    backtacking(visited, per)
                    per.pop()
                    visited[i] = 0
        
        nums.sort()
        visited = [0] * len(nums)
        res = []
        backtacking(visited, [])
        return res