'''
矩阵原地旋转，并且证明算法的正确性

 
new[col][n−row−1]=matrix[row][col]
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n < 2:
            return matrix

        # 上下对折
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[-(i + 1)][j] = matrix[-(i + 1)][j], matrix[i][j]

        # 按对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return 