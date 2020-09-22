# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/10  
# @Author  : XU Liu
# @FileName: 213.House Robber II.py


'''
题目要求：
给的数字是一个circle，也就是说，第一数字与最后一个数字是相邻的
'''

'''
[0, 1, 2, 3, 4, 5]
分三种情况
第一种情况： 1到4
第二种情况： 0到4
第三种情况： 1到5
找到这三种情况里面最大值
其实我们不需要比较三种情况，只要比较情况二和情况三就行了，因为这两种情况对于房子的选择余地比情况一大呀，房子里的钱数都是非负数，所以选择余地大，最优决策结果肯定不会小。

dp[i] = max(choose, not choose)
      = max(dp[i-2] + nums[i], dp[i-1])
base case:
    dp[0] = nums[0]
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        def count(nums, max_res):
            n = len(nums)
            dp_i = nums[0]
            dp_i2 = nums[0]

            for i in range(1, n):
                if i == 1:
                    dp_i = max(nums[0], nums[1])
                else:
                    temp = dp_i
                    dp_i = max(dp_i2 + nums[i], dp_i)
                    dp_i2 = temp
            return max(max_res, dp_i)
        
        m = len(nums)
        if m == 1:
            return nums[0]
        if m == 2 or m == 3:
            return max(nums)
        else:
            max_res = 0
            max_res = count(nums[0:m-1], max_res)
            max_res = count(nums[1:m], max_res)
            # max_res = count(nums[1:m-1], max_res)
        return max_res

