'''
输出字符串的全排列，同时要满足，相邻字符不能相同

时间复杂度为 O(n×n!)
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []
        
        nums.sort()

        def find(path):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for i in range(len(nums)):
                if visited[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == 1:
                    continue
                if len(path) > 0 and path[-1] == nums[i]:
                    continue
                    
                visited[i] = 1
                path.append(nums[i])
                find(path)
                path.pop()
                visited[i] = 0

            return 
        
        res = []
        visited = [0] * len(nums)
        find([])
        return res