# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/15  
# @Author  : XU Liu
# @FileName: 15.3Sum.py

'''
1. 题目类型：


2. 题目要求与理解：
    找到所有三个数相加为0的组合

'''

'''
暴力解法
三个for循环
时间复杂度过高 O(n**3)

优化from 小丁
step1  数组排序
step2  从最左边 i+1（最小值）和最右边 len(nums)-1（最大值）两个数字开始，加上 C 位，计算总和是否等于 0。
       如果大于 0，说明实力太强了，就把右侧的数字左移一位。
       如果小于 0，说明实力太弱了，就把左边的数字右移一位。
       当双指针碰到的时候，这轮循环结束，以该数字为 C 位的所有可能都已经尝试完毕了。
       这里要注意数组的去重，去重过程包含了遍历，也会增加时间复杂度，所以要优化，对于排序完成的数组来说，只要判断下相邻的数是否相等，如果相等就直接移动指针即可，这就完成了去重。

时间复杂度：O(n^2)
疑问点： 为什么不是nlogn?  for循环 * 二分搜索
因为这里的这个不是二分搜索，是左右指针
二分搜索的时候，是跳跃的，不是每一个数字都会被遍历到
这里的左右往中间走，最坏情况的时候，每个数字都会被遍历到
'''

'''
Time Limit Exceeded
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        n = len(nums)
        for i in range(n):
            l = i + 1
            r = n - 1
            
            while l < r:  # 不用等号
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] == 0:
                    if [nums[i], nums[l], nums[r]] not in res:  # 判断list是否在list里是可行的 
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        
        return res

'''
再优化
这里要注意数组的去重，去重过程包含了遍历，也会增加时间复杂度，所以我进行了优化，
对于排序完成的数组来说，只要判断下相邻的数是否相等，如果相等就直接移动指针即可，这就完成了去重。
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        n = len(nums)
        for i in range(n):
            # 这一个数跟上一个 数一样，上一轮已经考虑过了，去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l = i + 1
            r = n - 1
            
            while l < r:  # 不用等号
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] == 0:
                    #if [nums[i], nums[l], nums[r]] not in res:  # 有这一行的话， 时间复杂度是O(n),白白去重了，爆表
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 去重 下一个数跟现在是一样的，直接再移动一位
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:  # 易错 l是l-1， r是r+1
                        r -= 1
        return res


'''
res不要是list，set
set的时间复杂度是O(1)!!!!
小丁的方法过于繁琐
'''