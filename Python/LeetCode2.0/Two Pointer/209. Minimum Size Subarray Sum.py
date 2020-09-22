#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/26


'''
Two pointer - slide window
Steps:
    1. set i, j start at 0, 1
    2. move j until sum(nums[i:j + 1]) >= s
       move i
       if sum(nums[i:j + 1]) >= s, renew length
       else, still move i until sum(nums[i:j + 1]) < s
    3. repeat step2 until j out of range
    4. return length

Time O(N)
Space O(1)

Binary sort
Steps:
    1. sort nums
    2. set l, r start at 0, len(nums) - 1
        move l, r following next steps until l > r [l <= r ok]
    3. calculate mid = (l + r) // 2
    4. compare nums[mid] with s 
'''

# slide window
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        i = 0
        res = float('inf')
        Sum = 0

        for j in range(len(nums)):
            Sum += nums[j]
            if Sum >= s:
                while Sum >= s and i <= j:
                    res = min(res, (j - i + 1))
                    Sum -= nums[i]
                    i += 1
        if res == float('inf'):
            return 0
        else:
            return res

# prefix 超时
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums == []:
            return 0

        prefix = [0] * len(nums)
        for i, n in enumerate(nums):
            if i == 0:
                prefix[i] = n
            else:
                prefix[i] = prefix[i - 1] + n

        res = float('inf')
 
        for i in range(len(prefix)):
            for j in range(i, len(prefix)):
                Sum = prefix[j] - prefix[i] + nums[i]  # point
                if Sum >= s:
                    res = min(res, (j - i + 1))
        if res == float('inf'):
            return 0
        else:
            return res