#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/29  
# @Author  : XU Liu
# @FileName: 74.Search a 2D Matrix.py

'''
1. 题目类型：
    binary search

2. 题目理解以及解题思路：
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    关键点：
        l, r as 0, row*column - 1
        midVal = matrix[mid // column][mid % column]
        行是整数，列是余数

3. 输出输入以及边界条件：
input: 
output: 
corner case: 


4. 时间空间复杂度：
    时间复杂度 O(log(MN))
    空间复杂度 O(1)

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or matrix == [[]]:  # corner case
            return False

        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1
        while l <= r:
            mid = l + (r - l) // 2
            midVal = matrix[mid // n][mid % n]
            if target == midVal:
                return True
            if target < midVal:
                r = mid - 1
            else:
                l = mid + 1
        return False


'''
按行binary search
m是行数，n是一行内的个数
时间复杂度: O(mlongn)
空间复杂度：O(n) 
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [[]] or matrix == []:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        def find(i):
            arr = matrix[i]
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return True
                if arr[mid] > target:
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
            return False
            
            
        
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                if find(i) == True:
                    return True
        return False

'''
按行binary search
m是行数，n是一行内的个数
时间复杂度: O(mlongn)
空间复杂度：O(1)
'''
class Solution:
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix == [[]]:
            return False
        
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:

                l, r = 0, len(matrix[i]) - 1
                while l <= r:
                    mid = l + (r - l)//2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False