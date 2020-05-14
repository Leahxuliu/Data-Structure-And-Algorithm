# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/13 

'''
input: height:List[int],  the value of height is from 0 to inf,  the number of heights is from 2 to inf(n)
output: the most water: int
corner case: len(height) == 2, return min(height)

Method - Two pointer 
Steps:
    1. i: slow pointer, start at 0
       j: fast pointer, start at n - 1 
    2. calculate water = min(height[i], height[j]) * (j - i)
    3. if height[i] < height[j], move i, i+1, else, move j, j - 1
    4. repeat step2 and step3 until i = j
    5. choose max water

Time complexity: O(N)
Space: O(1)

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n =  len(height)
        if n == 2:
            return min(height)
        
        i, j = 0, n - 1
        res = 0
        while i < j:
            res = max(res, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res