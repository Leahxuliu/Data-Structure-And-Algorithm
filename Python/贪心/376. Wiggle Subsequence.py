'''
subsequence!!! 可以是不连续的

greedy + two point
positive: choose the most one
negative: choose the less one

1 17 5 10 5 16 8

[1,17,5,10,13,15,10,5,16,8]
    i j +1
      i  j 
         i j
           i  j
              i  j + 1 
                 i  j
                    i  j + 1
                       i   j +1

'''

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # wrong [0, 0]
        #if len(nums) <= 2:
        #    return len(nums)
        if len(nums) <= 1:
            return len(nums)
    
        count = 1
        start = False  # 易错 因为一开始的两个数字是相同的话，不能当作起始点
        i = 0
        j = 1
        while j < len(nums):
            temp = nums[j] - nums[i]
            if start == False:
                if temp != 0:
                    pre = temp
                    start = True
                    count += 1
                i = j
                j += 1
                continue

            if temp * pre < 0:
                pre = temp
                count += 1
                i = j
                j += 1
            else:
                if temp > 0 and nums[j] > nums[i]:
                    i = j
                if temp < 0 and nums[j] < nums[i]:
                    i = j
                j += 1
        return count
                
'''
贪心 优化

没有必要找最大或最小
因为最大最小是峰或者谷
'''

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        pre = nums[1] - nums[0]
        count = 1 + (pre != 0)
        
        for i in range(2, len(nums)):
            temp = nums[i] - nums[i - 1]                
            if temp * pre < 0 or (pre == 0 and temp != 0):
                pre = temp
                count += 1
        return count


