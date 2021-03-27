# 一共四种情况，无解，全部由左边构成，全部由右边构成，两边共通构成

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if nums[0] > x and nums[-1] > x:
            return -1
        '''
        dp = [-1] * len(nums)
        
        leftSum = 0
        for i in range(len(nums)):
            # choose
            leftSum =+ nums[i]
            while leftSum < x:
                
            # not choose
            
        return min(dp)
        '''
        
        leftSum = {}
        rightSum = {}
        
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            leftSum[count] = i + 1
        
        count = 0
        for i in range(1, len(nums) + 1):
            count += nums[-i]
            rightSum[count] = i
            
        res = float(inf)
        for k, v in leftSum.items():
            if k > x:
                break
            if k == x:
                res = min(res, v)
            
            else:
                temp = x - k
                if temp in rightSum:
                    if rightSum[temp] + v <= len(nums):
                        res = min(res, v + rightSum[x - k])
        
        if x in rightSum:
            res = min(res, rightSum[x])
        
        if res == float(inf):
            return -1
        else:
            return res


# 代码精简优化
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if nums[0] > x and nums[-1] > x:
            return -1
        
        leftSum = {}
        rightSum = {}
        
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > x:
                break
            leftSum[count] = i + 1
        
        count = 0
        for i in range(1, len(nums) + 1):
            count += nums[-i]
            if count > x:
                break
            rightSum[count] = i
            
        res = min(leftSum.get(x, float('inf')), rightSum.get(x, float('inf')),)
        for k, v in leftSum.items():
            temp = x - k
            if temp in rightSum:
                if rightSum[temp] + v <= len(nums):
                    res = min(res, v + rightSum[x - k])
        
        return res if res != float('inf') else -1