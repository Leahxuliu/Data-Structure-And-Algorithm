'''
300

'''

# DP

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        n = len(nums)
        dp = [1] * n 

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
    
# 耐心排序
'''
* 核心是二分搜索，类似小时候玩的纸牌接龙

- 每个堆上面的数，从左到右是递增的
- 每个堆是递减的（可相等）(每次放小的值在上面)
- 堆的个数也就是最长递增子序列
- 时间复杂度: O(n log(n))
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        def find(target, start, end):
            l = start
            r = end
            while l <= r:
                mid = l + (r - l) // 2
                if piles[mid] == target:
                    return mid
                elif piles[mid] < target:
                    l = mid + 1
                else:
                     r = mid - 1
            return l

        n = len(nums)
        piles = [float('inf')] * n 
        piles[0] = nums[0]
        count = 1

        for i in range(1, n):
            if nums[i] < piles[0]:
                piles[0] = nums[i]

            elif nums[i] > piles[count - 1]:
                piles[count] = nums[i]
                count += 1
            else:
                index = find(nums[i], 0, count - 1)
                piles[index] = nums[i]
        return count