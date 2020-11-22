class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        f = {}
        b = {}
        n = len(nums)
        
        sumO = 0
        sumJ = 0
        for i in range(n):
            f[i] = [sumO, sumJ]
            
            if i % 2 == 0:
                sumO += nums[i]
            else:
                sumJ += nums[i]
        
        sumO = 0
        sumJ = 0
        for i in range(n-1, -1, -1):
            b[i] = [sumO, sumJ]
            if i % 2 == 0:
                sumO += nums[i]
            else:
                sumJ += nums[i]
        

        res = 0
        for i in range(n):
            #print(f[i][0], f[i][1], b[i][0], b[i][1])
            if f[i][0] + b[i][1] == f[i][1] + b[i][0]:
                res += 1
        
        return res