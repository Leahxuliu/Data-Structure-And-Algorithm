# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/16  
# @Author  : XU Liu
# @FileName: 26.Remove Duplicates from Sorted Array.py

'''
1. 题目类型：


2. 题目要求与理解：
    一组sort过的数组，原地修改数组
    使得数组前面没有重复的数字，比如[0, 1, 1, 1, 2, 3] --> [0, 1, 2, 3, 1, 1]
    输出不重复的数字有几个，上面这个例子当中是4

3. 解题思路：
    前向型指针，i：slow指针， j：quick指针
    初始值 i==0, j==1
    arr[i] == arr[j] --> j继续往前走
    arr[i] != arr[j] --> i = i + 1

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
空间复杂度 O(1)
时间复杂度 O(N)
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
                      
        return i + 1