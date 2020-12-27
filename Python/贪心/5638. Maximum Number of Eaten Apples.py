'''
贪心 优先队列
先吃掉要过期的
'''

from heapq import *
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        n = len(apples)
        i = 0
        res = 0

        while heap or i < n:
            # 放入苹果
            if i < n and apples[i] > 0:
                heappush(heap, (days[i] + i, apples[i]))
            
            # 移除过期的苹果
            while heap and heap[0][0] <= i:  # 要有=
                heappop(heap)

            # 吃苹果
            if heap:
                d, num = heappop(heap)
                num -= 1
                res += 1
                if num > 0:
                    heappush(heap, (d, num))
            
            i += 1
        return res

#DFS 

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def DFS(i, j):
            n = len(grid)
            m = len(grid[0])

            if i == n:
                return j

            if grid[i][j] == 1 and j + 1 < m and grid[i][j + 1] == 1:
                return DFS(i + 1, j + 1)
            if grid[i][j] == -1 and j - 1 >= 0 and grid[i][j - 1] == -1:
                return DFS(i + 1, j - 1)
            return -1

        
        res = []
        for i in range(len(grid[0])):
            res.append(DFS(0, i))
        
        return res