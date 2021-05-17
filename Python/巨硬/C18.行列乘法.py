'''
311
两个非常大的稀疏矩阵做点乘，以及后序拓展
'''

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []

        for i in range(len(A)):

            level = []
            for x in range(len(B[0])):
                count = 0
                for j in range(len(A[i])):
                    temp = A[i][j] * B[j][x]
                    count += temp
                level.append(count)
            res.append(level)
        return res
