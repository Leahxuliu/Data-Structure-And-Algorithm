#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/29  
# @Author  : XU Liu
# @FileName: 209.Minimum Size Subarray Sum.py

'''
1. 题目要求：
长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
如果不存在符合条件的连续子数组，返回 0。

s = 7, nums = [2,3,1,2,4,3]
子数组 [4,3] 是该条件下的长度最小的连续子数组

如果你已经完成了 O (n) 时间复杂度的解法，请尝试 O (n log n) 时间复杂度的解法。

2. 理解：
0是正整数
可以是自己，一个值

3. 输出输入以及边界条件：
input: sum int; nums list[int]
output: int the length of the min size Subarray Sum
corner case: nums == None

4. 解题思路
思路一:
    暴力解法 brute force
    for i in range(n):
        for j in range(i,n):
            sum(nums[i:j+1])
    空间复杂度 O(1)
    时间复杂度 O(n**2)


思路二:
    滑动窗口
    1. 右窗口从左窗口所在位置出发，向右移动
    2. 和 >= sum, sum - nums[l], 左窗口+1
    （先固定住左边界，探索右边界；
      当sum比指定s大时，适当缩小左边界）

    空间复杂度 O(1)
    时间复杂度 O(N)

思路三:
    binary search
    空间复杂度 O(N)
    时间复杂度 O(NlogN)

'''

'''
Time Limit Exceeded
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        l, r = 0, 0
        n = len(nums)
        res = float('inf')
        
        while l < n-1:
            for r in range(l, n):
                Sum = sum(nums[l:r+1])
                if Sum >= s:
                    res = min(res, (r-l+1))
                if r == n-1:
                    l += 1
        if res == float('inf'):
            return 0
        else:
            return res

'''
思路二
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, Sum, res = 0, 0, float('inf')
        
        for r in range(len(nums)):
            Sum += nums[r]
            # while Sum >= s and l <= r: 可
            while Sum >= s and l <= r:
                res = min(res, (r - l + 1))
                Sum -= nums[l]  # 关键点
                l += 1  # l一定是在范围内，不必再加l的边界条件
        if res == float('inf'):
            return 0
        else:
            return res