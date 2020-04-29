# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/16  
# @Author  : XU Liu
# @FileName: 27.Remove Element.py

'''
1. 题目类型：


2. 题目要求与理解：
    一组sort过的数组，原地删除指定的值
    输出新的len，len后面的值不用管

3. 解题思路：
    前向型指针，i：slow指针， j：quick指针
    初始值 i==0, j==0
    arr[j] == val --> j += 1
    arr[j] != val --> i = i + 1, j = j + 1, nums[i] = nums[j]

    i是结果可放的位置
    但j是符合要求的值时，放到i上

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
空间复杂度 O(1)
时间复杂度 O(N)
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i