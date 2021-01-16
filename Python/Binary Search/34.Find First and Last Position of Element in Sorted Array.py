#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/27  
# @Author  : XU Liu
# @FileName: 34.Find First and Last Position of Element in Sorted Array.py


'''
1. 题目理解：
    一个从小到大排列的数组
    有重复数
    找到target数，最先开始的位置和结束的位置
    如果不存在这个数，输出[-1,-1]
    runtime complexity must be in the order of O(log n) --> binary search


2. 题目类型：
    binary search

3. 输出输入以及边界条件：
input: nums: List[int], target: int
output: int
corner case: None, 最小值比target大，最大值要比target小

4. 解题思路
    利用while l<=r这个条件
    在target数前和数后建立一个虚拟数的概念
    找到这个虚拟数的位置
    第一个位置：nums[l]==target
    最后一个位置：nums[r]==target
    比如nums = [5,7,7,8,8,10], target = 8
    开始：也就是找到第一个比4要小的最大值，return l
    结束：也就是找到第一个比4要大的最小值，return r
    

5. 时间空间复杂度：
    

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        # 如果没有这些条件， [2,2]，8就会报错，因为l会out of range
        if nums[0] > target:
            return [-1, -1]
        if nums[-1] < target:
            return [-1, -1]
        
        def findFirst(target, start):
            l = start
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:  # 继续往右边找
                    r = mid - 1
                else:
                    l = mid + 1
            return l if nums[l] == target else -1  # 返回l，易错

        def findLast(target, start):
            l = start
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r if nums[r] == target else -1
        
        first = findFirst(target, 0)
        print(first)
        if first == -1:
            return [-1, -1]
        last = findLast(target, first)
        return [first, last]



x = Solution()
print(x.searchRange([5,7,7,8,8,10], 8))