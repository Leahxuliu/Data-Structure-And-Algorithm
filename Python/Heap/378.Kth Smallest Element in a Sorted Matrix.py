# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/02  
# @Author  : XU Liu
# @FileName: 378.Kth Smallest Element in a Sorted Matrix.py

'''
1. 题目要求：


2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
按行遍历
len(heap) < k, heappush
len(heap) >= k, heappushpop

5. 空间时间复杂度
Time complexity: O(n^2 * log(k))
Space: O(k)
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
       
        n = len(matrix)
        heap = []
        
        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heappush(heap, -matrix[i][j])
                else:
                    heappushpop(heap, -matrix[i][j])
        return -heappop(heap)