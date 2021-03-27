#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/28  
# @Author  : XU Liu
# @FileName: 80.Remove Duplicates from Sorted Array II.py

'''
1. 题目要求：
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O (1) 额外空间的条件下完成。

2. 理解：


3. 输出输入以及边界条件：
input: list[int] a sorted array nums
output: int 
corner case: None --> 0

4. 解题思路
快慢双指针
[1, 1, 1, 2, 2, 3]
 i  j

最终i走过的路径
[1, 1, 1, 2, 2, 3]
[1, 1, 2, 2, 3, 3]+
 i  i  i  i  i



5. 空间时间复杂度
空间 O(1)
时间 O(N)

'''

'''
例子
[0,0,1,1,1,1,2,3,3]
'''

# 不太理解
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        i, j = 0, 1
        count = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                if count == 2:
                    i += 1
                    nums[i] = nums[j]  # key
                    j += 1
                else:
                    j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
                count = 1
        return i + 1


'''
不能超过两个，不包括两个
双指针
slow指针表示可以放的前一个位置
fast去找下一个与slow指针所在位置不同的值

　　　1,　1,　1,　2,　2,　3
     s  s 
         f   f   
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        
        slow = 0
        fast = 1
        count = 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                if count == 1:
                    slow += 1
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    count += 1
                fast += 1
            else:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
                fast += 1
                count = 1
        return slow + 1
