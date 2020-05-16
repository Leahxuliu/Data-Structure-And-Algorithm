'''
Method - BFS
Steps:
    1. create visited and graph
            graph: dict, key:vertex, value:[vertex, value]
                    eg:{a:[b, 2.0]}
    2. use visited and graph to calculate queries
    
'''

from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if equations == [[]] or equations == []:
            return []
        
        visited = defaultdict(int)
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            graph[equations[i][0]].append([equations[i][1], values[i]])
            graph[equations[i][1]].append([equations[i][0], 1/values[i]])
        
        def BFS(x, y):
            queue = deque()
            used = [x]
            loop_res = 0
            
            for out in graph[x]:
                if out[0] == y:
                    loop_res = out[1]
                else:
                    queue.append([out[0], out[1]])
                    used.append(out[0])

                    while queue:
                        index, temp =  queue.pop()
                        for out_index in graph[index]:
                            if out_index[0] == y:
                                loop_res = temp * out_index[1]
                                queue = deque()
                            else:
                                if out_index[0] not in used:
                                    queue.append([out_index[0], temp*out_index[1]])
                                    used.append(out_index[0])
            if loop_res == 0:
                return res.append(-1.0)
            else:
                return res.append(loop_res)
                                
        res = []
        for x, y in queries: 
            if x not in graph or y not in graph:
                res.append(-1.0)
            elif x == y:
                res.append(1.0)
            else:
                BFS(x, y)
        return res
                                    
                            
# 简化
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        if equations == None:
            return []
        
        graph = defaultdict(dict)
        for (x,y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0/val
        print(graph)
        res = []
        for i,j in queries:
            if i not in graph or j not in graph:
                res.append(-1.0)
            else:
                if i == j:
                    res.append(1.0)
                else:
                    res.append(self.count(graph, i, j))
        return res
        
    def count(self, graph, i, j):
        queue = deque()
        visited = set()
        queue.append([i, 1.0])
        
        while queue:
            node, multi = queue.popleft()
            if node == j:
                return multi
                
            visited.add(node)
            for elem in graph[node]:
                if elem not in visited:
                    queue.append([elem, multi * graph[node][elem]])
        return -1.0  
