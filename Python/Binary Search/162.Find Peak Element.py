#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/29  
# @Author  : XU Liu
# @FileName: 162.Find Peak Element.py

'''
1. 题目类型：
    binary search

2. 题目要求：
    找峰值所在的index
    nums[i] ≠ nums[i+1]
    有多个峰值的时候，随意输出一个峰值即可

3. 解题思路：
    峰值i
    nums[i-1] < nums[i] > nums[i+1]
    while l + 1 < r:
    
4. 输出输入以及边界条件：
input: nums: List[int]
output: int
corner case: 


5. 时间空间复杂度：
    Time complexity: O(logN)
    Space O(1)

'''


'''
错误尝试
比如 nums：[1]
这样写的话，len(nums)要>=3
while l =< r: / l = mid + 1 / r = mid -1  --> list index out of range
while l =< r: / l = mid  / r = mid  --> output:None

'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums == None:
            return
        
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) //2
            
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:  # len(nums) == 1,2时 会报错
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid
            elif nums[mid] > nums[mid + 1]:
                r = mid


'''
找峰值的模版
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return []

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid
            else:
                r = mid
        if nums[l] < nums[r]:
            return r
        else:
            return l


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:  # return peak value's index
        if nums is None:
            return None

        l, r = 0, len(nums) - 1
        while l < r :
            mid = l + (r - l) // 2
            if nums[mid] <= nums[mid + 1]:
                l = mid + 1  # 峰值肯定不是mid
            if nums[mid] > nums[mid + 1]:
                r = mid
        
        return l