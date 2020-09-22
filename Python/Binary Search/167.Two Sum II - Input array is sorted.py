#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/24  
# @Author  : XU Liu
# @FileName: 167.Two Sum II - Input array is sorted.py

'''
1. 题目要求：
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

2. 理解：
给的array里面，两数相加=target
输出这两数的index 注意 要输出1-based

3. 题目类型：
binary search
有target类型

4. 输出输入以及边界条件：
input: numbers: List[int], target: int
output: List[int] 两数的index
corner case:  numbers == None
              min(numbers)  > target

5. 解题思路
    方法一: 普通的遍历 --> Time Limit Exceeded
    方法二: binary search 
    易错点：不能自己加自己
    for i in range(len(numbers) - 1):
            for j in range(i+1, len(numbers)): --> binary search

'''

'''
方法一
'''

class Solution:
    def twoSum(self, numbers, target):
        if numbers == None:
            return []
        if numbers[0] > target:
            return []
        
        for i in range(len(numbers) - 1):
            for j in range(i+1, len(numbers)):  # range易错
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]


'''
方法2
第16个case，超时
两个for循环，超时
'''

class Solution:
    def twoSum(self, numbers, target):
        if numbers == None:
            return []
        if numbers[0] > target:
            return []

        for i in range(len(numbers)-1):  # range范围易错
            for j in range(i+1, len(numbers)):
                l, r = i+1, len(numbers) - 1
                while l <= r:
                    mid = l + (r - l) //2
                    # mid = (r+l)//2 上面那样写是为了防止计算机超限

                    if target == numbers[i] + numbers[mid]:
                        return [i+1, mid+1]
                    if target < numbers[i] + numbers[mid]:
                            r = mid - 1
                    elif target > numbers[i] + numbers[mid]:
                            l = mid + 1

'''
方法三
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers == None:
            return []
        
        def find(target, arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l)//2
                if target == arr[mid]:
                    return mid
                elif target > arr[mid]:
                    l = mid + 1
                elif target < arr[mid]:
                    r = mid - 1
            return -1
        
        for i in range(len(numbers) - 1):
            new_T = target - numbers[i]
            index = find(new_T, numbers[i+1:])
            if index != -1:
                return [i+1, (i+1+index+1)]


x = Solution()
print(x.twoSum([1,2,3,4,4,9,56,90],8))