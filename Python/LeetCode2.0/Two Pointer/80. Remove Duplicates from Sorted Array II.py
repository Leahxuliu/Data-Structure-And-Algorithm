#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/18

'''
Method - Two pointer (fast and slow pointer)
Steps:
    1. set i, j start at 0, 1
    2. compare nums[i] and nums[j], and count how many times does nums[i] appear
    3. 


'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        i, j = 0, 1
        count = 1
        while j <= len(nums) - 1:
            if nums[i] == nums[j]:
                count += 1
                if count > 2:
                    j += 1
                else:
                    i += 1
                    nums[i] = nums[j]  # 易错， 如果没有这行的话， [0,0,1,1,1,1,2,3,3] --> [0,0,1,1,2,3,2]
                    j += 1
            
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
                count = 1
            
        return i + 1