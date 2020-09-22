#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/27  
# @Author  : XU Liu
# @FileName: 81.Search in Rotated Sorted Array II.py

'''
1. 题目理解：
    旋转
    有重复数字，例如 [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]
    如果有target数字就return True
    没有就False

2. 题目类型：
    binary search里面的旋转

3. 输出输入以及边界条件：
input: nums: List[int], target: int
output: bool
corner case: nums == None

4. 解题思路
    旋转有重复跟没有重复，就一个地方不一样
    if nums[l] == nums[mid]:
        l += 1  # 注意！！！

5. 时间空间复杂度：
    

'''


class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            elif nums[l] == nums[mid]:
                l += 1  # 注意！！！
            
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

x = Solution()
print(x.search([1,3,1,1,1],3))