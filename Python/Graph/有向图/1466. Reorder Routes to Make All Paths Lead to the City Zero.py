'''
构建graph的时候，“忽略了”方向,如同无向图那样构建
但是，用0表示j->i,1表示i->j
BFS遍历，如果遇到的边是1，也就是要变更的边
'''
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        if n < 2:
            return 0
        
        graph = [[] for _ in range(n)]
        for i, j in connections:
            graph[i].append((j, 1))
            graph[j].append((i, 0))
        
        visited = [0] * n

        count = 0
        for i in range(n):
            if visited[i] == 0:
                queue = deque()
                queue.append(i)
                visited[i] = 1

                while queue:
                    node = queue.popleft()
                    for out, val in graph[node]:
                        if visited[out] == 0:
                            count += val
                            queue.append(out)
                            visited[out] = 1
        return count 


# DFS

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [0] * n 

        for i, j in connections:
            graph[i].append((j, 1))
            graph[j].append((i, 0))
        

        def travesal(i):
            nonlocal res
            if visited[i] == 1:
                return 
            
            visited[i] = 1
            for out, cost in graph[i]:
                if visited[out] == 0:
                    res += cost
                    travesal(out)
            return 
        
        res = 0
        travesal(0)
        return res
