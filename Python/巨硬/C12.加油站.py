'''
一辆汽车，从0要开到n，路线上分布着kk个加油站（0号点必有）
每个加油站可以加a_i油，（1油可以跑1km），假设油箱初始为0，无装油上限,若可以跑nkm
求最少加油次数，不能就输出-1
'''

'''
贪心 + heap？
'''



'''
类似 45 跳跃
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:  # 易错
            return 0
        
        count = 1
        maxVal = nums[0]
        nextVal = nums[0]
        n = len(nums)

        for i in range(n):
            if i > maxVal:
                return -1
            
            nextVal = max(nextVal, i + nums[i])
            if i == maxVal and i != n - 1:
                count += 1
                maxVal = nextVal
        return count

'''
更好理解？
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        next_step = 0
        maxVal = 0
        count = 0
        
        for i, each in enumerate(nums):
            if i + each > next_step:
                next_step = i + each 
            
            if i == maxVal and i != len(nums) - 1:
                count += 1
                maxVal = next_step
        return count



'''
55 跳跃
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == []:
            return True
        if len(nums) == 1:
            return True
        
        maxVal = 0
        for i in range(len(nums)):
            if maxVal >= i and i + nums[i] > maxVal:
                maxVal = i + nums[i]
        
        return maxVal >= len(nums) - 1