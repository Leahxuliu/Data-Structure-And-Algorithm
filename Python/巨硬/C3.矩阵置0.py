'''
73
给定一个二维矩阵，包括0和非0，把0所在的行和列都设置为0


* 第一行 第一列作为标记
* 第一行 第一列单独考虑
'''
'''
用matrix第一行和第一列记录该行该列是否有0,作为标志位
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        flag_row = False
        flag_col = False

        # check if the first column have 0
        for i in range(m):
            if matrix[0][i] == 0:
                flag_col = True
                break 
        
        # check first row
        for i in range(n):
            if matrix[i][0] == 0:
                flag_row = True
                break
        
        # travesal 
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # change to 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

    
        # change first row and first column
        if flag_col:
            for i in range(m):
                matrix[0][i] = 0
        if  flag_row:
            for i in range(n):
                matrix[i][0] = 0
        return 

