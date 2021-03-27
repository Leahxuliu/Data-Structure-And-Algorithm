# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/16

# 注意与11题区分

# brute force 超时
'''class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights == []:
            return 0
        if len(heights) == 1:
            return heights[0]
        max_area = 0
        for i in range(len(heights)):  # 易错， 注意可以是只有自己一个柱子
            min_high = heights[i]
            for j in range(i, len(heights)):
                min_high = min(min_high, heights[j])
                max_area = max(max_area, (j - i + 1) * min_high)
        return max_area'''


# https://www.youtube.com/watch?v=VNbkzsnllsU

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights == []:
            return 0
        
        heights.append(0)
        stack = [-1]
        res = 0
        for i, each in enumerate(heights):
            while each < heights[stack[-1]]:
                h = heights[stack.pop()]
                res = max((i - stack[-1] - 1) * h, res)  # 难点，i是后面短的位置，stack[-1]是前面短的位置，所以改宽度是后面短的位置-前面短的位置 -1
            stack.append(i)
        return res