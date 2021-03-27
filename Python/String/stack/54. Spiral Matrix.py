# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/21

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # coner case
        if matrix == [] or matrix == [[]]:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [x[0] for x in matrix]

        l, r, t, b = 0, n - 1, 0, m - 1
        res = []
        while l <= r and t <= b:
            for column in range(l, r + 1):
                res.append(matrix[t][column])
            for row in range(t + 1, b + 1):
                res.append(matrix[row][r])
            
            if l < r and t < b:
                for column in range(r - 1, l, -1):
                    res.append(matrix[b][column])
                for row in range(b, t, -1):
                    res.append(matrix[row][l])
            
            l += 1
            r -= 1
            t += 1
            b -= 1
        return res