'''
54
59
'''

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
            # 左 含左右端点
            for column in range(l, r + 1):
                res.append(matrix[t][column])
            # 下 含右下端点
            for row in range(t + 1, b + 1):
                res.append(matrix[row][r])
            
            # 除去只有一行或者一列的情况
            # 比如只有一列的时候左下端点和右下端点是同一个端点
            if l < r and t < b:
                # 右 不含端点
                for column in range(r - 1, l, -1):
                    res.append(matrix[b][column])
                # 上 含左下端点
                for row in range(b, t, -1):
                    res.append(matrix[row][l])
            
            l += 1
            r -= 1
            t += 1
            b -= 1
        return res