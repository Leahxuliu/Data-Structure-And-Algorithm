# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16  
# @Author  : XU Liu
# @FileName: 18.4Sum.py

'''
1. 题目类型：


2. 题目要求与理解：


3. 解题思路：
    sort 数组
    四个数相加
    两个数遍历
    剩下两个数用左右指针

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    时间复杂度：O(N**3)

'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        all_res = set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                l = j + 1
                r = n -1
                
                while l < r:
                    sums = nums[i] + nums[j] + nums[l] + nums[r]
                    if sums == target:
                        all_res.add((nums[i], nums[j], nums[l], nums[r]))
                        r -= 1
                        l += 1
                    elif sums > target:
                        r -= 1
                    elif sums < target:
                        l += 1
        all_res = list(all_res)
        return all_res