#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/26  
# @Author  : XU Liu
# @FileName: 33.Search in Rotated Sorted Array.py

'''
1. 题目理解：
    找到目标值
    给到的arr是部分sort，都是升序，旋转
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand
    输出target的index（0-based）
    如果不存在target就输出-1

2. 题目类型：
    很常考
    binary search
    有target，部分sort
    旋转

3. 输出输入以及边界条件：
input: nums: List[int], target: int
output: int
corner case: None

4. 解题思路
    1. binary search
    2. 核心 arr[mid]与arr[mid+1]之间的关系
           arr[mid]与arr[r]/arr[l]之间的关系

5. 时间空间复杂度：
    时间复杂度：O(log n)
    空间复杂度：O(1) 

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:  # corner case
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            if nums[l] < nums[mid]:  # 左边是sorted
                if nums[l] <= target < nums[mid]:  # T在左边sorted部分内
                    r = mid - 1
                else:  # T在右边的unsorted内
                    l = mid + 1
            elif nums[l] == nums[mid]:  # 只有两个数字的时候，下一轮就return -1
                l = mid + 1  # 或者l += 1
            elif nums[l] > nums[mid]:  # 左边是unsorted,右边是sorted
                if nums[mid] < target <= nums[r]:  # T在右边sortedd内
                    l = mid + 1
                else:
                    r = mid - 1
        return -1




