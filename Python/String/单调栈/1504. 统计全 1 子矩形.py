'''
方案一
枚举法

https://leetcode-cn.com/problems/count-submatrices-with-all-ones/solution/tong-ji-quan-1-zi-ju-xing-by-leetcode-solution/
动图 简单易懂
'''


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        res = 0
        height = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    height[i][j] = 0
                else:
                    if j == 0:
                        height[i][j] = 1
                    else:
                        height[i][j] = height[i][j - 1] + 1

                # 不能是col = min(height[i][j], height[k][j])
                # 比如下面最上一行的min是1而不是min（2，2）
                '''
                2
                1
                2
                '''
                col = height[i][j]
                for k in range(i, -1, -1): 
                    col = min(col, height[k][j])
                    if col == 0:
                        break
                    res += col
                
        return res



