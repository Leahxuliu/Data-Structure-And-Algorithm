# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/17

'''
Method - monotone stack
[
  [1, 0, 1, 0, 0],
  [1, 0, 1, 2, 3],
  [1, 2, 3, 4, 5],
  [1, 0, 0 ,1, 0]
]

time: O(NM)
Space:O(M)

'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == [] or matrix == [[]]:
            return 0
        
        size = 0
        temp = [0] * (len(matrix) + 1)
        for j in range(len(matrix[0])):
            stack = [-1]
            for i in range(len(matrix) + 1):  # 这里加一是因为temp.append(0),在monoston的时候，能够全部比完
                if i <= len(matrix) - 1:
                    if matrix[i][j] == '1':
                        temp[i] += 1
                    else:
                        temp[i] = 0
        
                while temp[i] < temp[stack[-1]]:
                    h = temp[stack.pop()]
                    w = i - stack[-1] - 1
                    size = max(size, h * w)
                stack.append(i)
        return size


'''
DP
dp[i][j]: i,j这个点，最大宽度
1. 每一行的宽度 
    if matrix[i][j] == '1'
        dp[i][j] = dp[i][j - 1] + 1
    else, dp[i][j] = 0
2. 找以i，j为右下角时，最大面积
    从下往上遍历
    dp[i][j] --> dp[0][j]
'''

'''
DP
dp[i][j]: i,j这个点，最大宽度
1. 每一行的宽度 
    if matrix[i][j] == '1'
        dp[i][j] = dp[i][j - 1] + 1
    else, dp[i][j] = dp[i][j - 1]
2. 找以i，j为右下角时，最大面积
    从下往上遍历
    dp[i][j] --> dp[0][j]

超时
time: O(N^2M)
space: O(NM)
'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == [] or matrix == [[]]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        size = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i][j - 1] + 1
                
                minWeight = dp[i][j]
                for r in range(i, -1, -1):
                    minWeight = min(minWeight, dp[r][j])
                    h = i - r + 1
                    size = max(size, minWeight * h)
        return size

'''
Method - DP - 每个点的最大高度

不断向上方遍历，直到遇到“0”，以此找到矩形的最大高度。
向左右两边扩展，直到无法容纳矩形最大宽度。

高 heigh == dp
leftmost L
rightmost R

与monotone stack像
'''
# 错 不理解 需要看官方答案后进行订正
class Solution:
    def maximalRectangle(self, matrix):
        if matrix == [] or matrix == [[]]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [-1] * n  # 起始位置index = 0
        right = [n] * n  #起始位置是最右边，index = n - 1
        height = [0] * n
        size = 0

        for i in range(m):
            cur_left = 0
            cur_right = 0
            # updata height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1

            # updata left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    cur_left = j + 1

            # updata right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    cur_right = j - 1
            
            for j in range(n):
                size = max(size, height[j] * (right[j] - left[j] + 1))
        
        return size

