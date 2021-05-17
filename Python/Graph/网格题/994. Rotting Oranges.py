'''
一个rotten orange破坏一个component里面的orange， 最少的时间：BFS的层数
最后再check一下是不是所有的orange都rotten了

[[2,1,1],[1,1,1],[0,1,2]]
可以从两头开始，所以一开始就要把所有烂的位置都放入queue
'''
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == [] or grid == [[]]:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        visited = [[0] * m for _ in range(n)]

        queue = deque()
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = 1

        res = 0
        while queue:
            len_q = len(queue)
            res += 1
            for _ in range(len_q):
                x, y = queue.popleft()
                for (x2, y2) in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
                        continue
                    if visited[x2][y2] == 0 and grid[x2][y2] == 1:
                        queue.append((x2, y2))
                        visited[x2][y2] = 1
                        grid[x2][y2] = 2

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        # 一开始就烂的那一层不算
        return res - 1 if res > 0 else 0

