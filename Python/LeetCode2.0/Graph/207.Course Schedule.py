'''
I. Clarify
    Question:
    Courses: [0, numCourses - 1]
    [0, 1] means before taking course 0, you should finish 1  1-->0
    circle --> False
    no circle --> True
    
II. Method
    A. DFS - [-1, 0, 1]
        1. build visited and graph
        2. scan by DFS
        3. if the node's neighbor vertex is visiting(0) --> have circle --> False
    
    B. Topo Sort
        1. build indegree and outdegree
        2. add the vertexs which indegree is 0 into the queue
        3. traverse the neighbors of these vertexs
        4. each time, indegree - 1
        5. when the indegree at the vertex == 0, add into queue
        6. after scan, if indegree has value other than 0 --> have circle --> False
        (先把indegree是0的点加入到queue， 然后遍历这些点的neighbors，
        每遍历一次，其点的indegree都减一，当此点的indegree等于0时，加入queue，
        最终indegree里有不是0的，则说明有环)

'''
# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        
        visited = [-1] * numCourses
        graph = [[] for i in range(numCourses)]
        
        for i, j in prerequisites:
            graph[j].append(i)
        
        def dfs(i):
            if visited[i] == 1:
                return True
            if visited[i] == 0:
                return False
            
            visited[i] = 0
            for out in graph[i]:
                if dfs(out) == False:
                    return False
                
            visited[i] = 1
            return True
        
        for i in range(numCourses):
            if visited[i] == -1:
                if dfs(i) == False:
                    return False
        return True


# Topo sort
from collections import deque 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        
        indegree = [0] * numCourses
        outdegree = [[] for _ in range(numCourses)]
        
        for x, y in prerequisites:
            indegree[x] += 1
            outdegree[y].append(x)
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            index = queue.popleft()
            for out in outdegree[index]:
                indegree[out] -= 1
                if indegree[out] == 0:
                    queue.append(out)
                            
        return indegree == [0] * numCourses
                        