'''
41. First Missing Positive
'''
'''
有重复的情况！！！！
'''


'''
brout force
先排序，再遍历

1. 最小正数大于1，那么直接输出1
2. 数与数之间丢失的数
3. 正数都相连的话，返回最后一个数+1
'''
def firstMissingPositive(self, nums: List[int]) -> int:
    if nums == []:
        return 1
    
    nums = list(set(nums))
    nums.sort()
    n = len(nums)
    i = 0

    while i < n:
        if nums[i] <= 0:
            i += 1         
        else:
            if nums[i] > 1:
                return 1

            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            
            if i == n - 1:
                return nums[-1] + 1
            else:
                return nums[i] + 1
    return 1
    
'''
原地hash
index  0 1 2 3 4 5
val    1 2 3 4 5 6

遍历number 把number放到相应的index上，不存在的就不放
第一个index与val不匹配的就是res
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == []:
            return 1
        
        n = len(nums)
        for i in range(n):
            while nums[i] - 1 != i and 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:  # 用while，不断的进行调换，而不是一次调换
                swap = nums[i] - 1  # 一定要拿出来写 nums[nums[i] - 1]是错误的
                nums[i], nums[swap] = nums[swap], nums[i]
                
        
        for i in range(n):
            if nums[i] - 1 != i:
                return i + 1
        
        # [1]
        return n + 1