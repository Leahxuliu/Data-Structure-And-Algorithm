#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/29  
# @Author  : XU Liu
# @FileName: 744.Find Smallest Letter Greater Than Target.py

'''
1. 题目类型：
    binary search

2. 题目理解以及解题思路：
    找到列表中大于给定目标的最小元素 --> return r

3. 输出输入以及边界条件：
input: letters: List[str], target: str
output: str
corner case: None


4. 时间空间复杂度：
    

'''

'''
错误
letter里面有重复的
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = l + (r - l)//2
            
            if ord(letters[mid]) == ord(target):
                if mid == len(letters) - 1:
                    return letters[0]
                else:
                    return letters[mid + 1]
            elif ord(letters[mid]) > ord(target):
                r = mid - 1
            elif ord(letters[mid]) < ord(target):
                l = mid + 1
        return letters[l]
            

'''
订正
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if letters[mid] == target:
                l = mid + 1
            if ord(target) < ord(letters[mid]):
                r = mid - 1
            else:
                l = mid + 1
        if l > len(letters) - 1:
            return letters[0]
        else:
            return letters[l]
