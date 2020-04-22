#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/28  
# @Author  : XU Liu
# @FileName: 240.Search a 2D Matrix II.py

'''
1. 题目类型：
    binary search
    二维
    an m x n matrix

2. 题目理解以及解题思路：
    从左到右升，从上到下升，下一行第一个数不一定比上一行最后一个数小
    （Integers in each row are sorted in ascending from left to right.
      Integers in each column are sorted in ascending from top to bottom.）
    找target数，有就是True，没有就是False
    
3. 输出输入以及边界条件：
input: matrix：List[List[int]]，target: int
output: bool
corner case: None


4. 时间空间复杂度：
    方式一：
    延矩阵对角线遍历，对对角线的点的行和列进行二分法求值
    MlogN

    方式二：
    搜索空间约简法
    M+N

'''

'''
A. brute force - scan every node
    Method:
        1. corner case
        2. use two for loop to scan every node, if has, return True, else return False
    Time complexity: O(MN), M is row number, N is colunm number
    Space: O(1)
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False


'''
B. binary search
    Method:
        1. corner case
        2. traversal every row
            use binary search to find the target in the row
    Time complexity: O(MlogN)
    Space: O(1)
易错点：无
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        
        def find(row):
            l, r = 0, len(row) - 1
            while l <= r:
                mid = l + (r - l)//2
                if row[mid] == target:
                    return True
                if row[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
            
        for row in matrix:
            if row[0] <= target <= row[-1]:
                if find(row) == True:
                    return True
        return False


'''
corner case:
    1. matrix is None/[[]] -> False
    2. target is None -> False
C. diagoal bianry search
    Method:
        1. corner case
        2. search from the left-up part of matrix to the right- bottom, i node
            binary search i node's horizontal and vertical element
    Time Complexity: O(logN!) < O(NlogN), N is min(m, n) m, n is row numbers, column numbers
    Space: O(1)
易错点：
    r的边界应该是 m/n - 1，这个减一不能忘
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        def horizontal(i):
            l, r = i, n - 1
            while l <= r:
                mid = l + (r-l)//2
                midVal = matrix[i][mid]
                if midVal == target:
                    return True
                elif midVal > target:
                    r = mid - 1
                elif midVal < target:
                    l = mid + 1
            return False
            
        def vertical(i):
            l, r = i, m - 1
            while l <=r:
                mid = l + (r-l)//2
                midVal = matrix[mid][i]
                if midVal == target:
                    return True
                elif midVal > target:
                    r = mid - 1
                elif midVal < target:
                    l = mid + 1
            return False
        
        for i in range(min(m,n)):  # 对角线上点的个数=min(m,n)
            print(i)
            if matrix[i][i] == target:
                return True
            if matrix[i][i] < target <= matrix[i][n-1]:
                if horizontal(i) == True:
                    return True
            if matrix[i][i] < target <= matrix[m-1][i]:
                if vertical(i) == True:
                    return True
        return False

'''
D.search space reduction
    Method:
        1. corner case
        2. from left bottom [len(matrix)][0] i,to search
            if i < target, move up
            if i == target return True
            if i > target, move right
    Time complexity: O(m + n)
    Space: O(1)
易错点：
    1.并不是每个格子都扫到，其实只扫了一行和一列，故tO(m + n)
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:  # corner case
            return False
        if matrix == [[]]:
            return False
        if target == 0:
            return False

        i = len(matrix) - 1
        j = 0

        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False