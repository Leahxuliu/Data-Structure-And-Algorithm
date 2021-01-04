# 超时
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in nums[1:]:
            prefix.append(prefix[-1] + i)
        
        def DFS(start, ind):
            if len(ind) == 2:
                left = prefix[ind[0]]
                mid = prefix[ind[1]] - left
                right = prefix[-1] - left - mid
                if left <= mid and mid <= right:
                    self.res += 1
                return
            
            for i in range(start, len(nums) - 1):
                ind.append(i)
                DFS(i + 1, ind)
                ind.pop()
                
            return
        
        self.res = 0
        DFS(0, [])
        return self.res % (10 ** 9 + 7)

# 超时
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in nums[1:]:
            prefix.append(prefix[-1] + i)
        
        res = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                left = prefix[i]
                mid = prefix[j] - left
                right = prefix[-1] - left - mid
                if left <= mid and mid <= right:
                    res += 1
        return res % (10 ** 9 + 7)