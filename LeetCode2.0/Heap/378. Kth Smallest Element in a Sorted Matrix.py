#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/23


'''
Method - heap
Steps:
    1. create heap
    2. traverse integers, matrix[i][j]
    3. if len(heap) < k, heappush(heap, -matrix[i][j])
        else, heappushpop(heap, -matrix[i][j]) 
    4. return -heappop(heap)

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