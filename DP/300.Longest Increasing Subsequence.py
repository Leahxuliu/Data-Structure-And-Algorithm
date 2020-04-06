# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/06  
# @Author  : XU Liu
# @FileName: 300.Longest Increasing Subsequence.py

'''
1. 题目类型：
    dp

2. 题目要求与理解：
    找递增子序列最大是几


'''

'''
解题思路：
    if i == 0:
        dp[i] == 1
    elif arr[i] > arr[i-1]:
        dp[i] == dp[i-1] + 1
    elif arr[i] <= arr[i-1]:
        dp[i] == dp[i-1]

报错
nums: [4,10,4,3,8,9]
dp:[1, 2, 2, 2, 3, 4]

'''

class Solution:
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        
        n = len(nums)
        
        dp = [0] * n
        
        for i in range(n):
            if i == 0:
                dp[i] = 1
            elif nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            elif nums[i] <= nums[i-1]:
                dp[i] = dp[i-1]
        return dp[n-1]


'''
改进
比如：nums[5] = 3，既然是递增子序列，我们只要找到前面那些结尾比 3 小的子序列，然后把 3 接到最后，就可以形成一个新的递增子序列，而且这个新的子序列长度加一。

订正状态转移方程
base从0改成1
for从1开始
i: range(1,len(nums))
j: range(i)   易错

if nums[i] > nums[j]:
    dp[i] = max(dp[i], dp[j]+1)

更改output
不是dp[len(nums)]
而是max(dp)

时间复杂度 O(N^2)
空间复杂度 O(N)
'''

class Solution:
    def lengthOfLIS(self, nums):
        
        if nums == []:
            return 0
        
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


'''
二分查找解法
时间复杂度 O(NlogN)
patience game (小时候电脑里面的纸牌接龙)
patience sort
    建桶规则:如果没有桶,新建一个桶;如果不符合入桶规则那么新建一个桶
    入桶规则:只要比桶里最上边的数字小即可入桶,如果有多个桶可入,那么按照从左到右的顺序入桶即可
性质：
每个桶最上面的那个数，从左到右是从小到大排列的
牌的桶数就是LIS

'''

def lengthOfLIS2(nums):
    if nums == []:
        return 0
    
    n = len(nums)
    piles = 0
    arr = [0] * n
    arr[0] = nums[0]

    def BinarySearch(arr, target, piles):
        l, r = 0, piles
        while l <= r:
            mid = l + (r - l) //2
            if arr[mid] == target:
                return mid  # 相等的时候，放在相等的上面
            elif arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
        return l  # 易错

    for i in range(1, n):
        if nums[i] < arr[0]:  # arr的数字是sort的，从小到大
            arr[0] = nums[i]
        
        elif nums[i] > arr[piles]:  # 建立新的堆
            arr[piles + 1] = nums[i]
            piles += 1
        
        else:
            arr[BinarySearch(arr, nums[i], piles)] = nums[i]  # 改变原来堆上面的数字
    
    return (piles + 1)

print(lengthOfLIS2([4,10,4,3,8,9]))

