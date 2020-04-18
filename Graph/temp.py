# True: 有环
# False: 没有环
# 无环：其访问过的节点有且只有一个，并且是其节点的上一个节点（parent_index)

class Graph:
    def findCircle(self, nums, pairs):
        if nums == None:
            return False
        if pairs == None:
            return False
        
        visited = [0] * nums
        graph = [[] for _ in range(nums)]
        
        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)
            
        def dfs(index, parent):
            visited[index] = 1
            
            for j in graph[index]:
                if visited[j] == 0:
                    if dfs(j, index) == True:
                        return True
                elif j != parent:
                    return True
            return False
            
            
        for i in range[nums]:
            if visited[i] == 0:
                if dfs(index, -1) == True:
                    return True
        return False


# True: 有环
# False: 没有环

from collections import deque, defaultdict
class Graph:
    def findCircle(self, nums, pairs):
        if nums == None or pairs == None:
            return False
        
        visited = [0] * nums
        graph = defaultdict(set)
        queue = deque()
        
        for i, j in pairs:
            graph[i].add(j)
            graph[j].add(i)
            
        for i in range(nums):
            if visited[i] == 0:
                queue.append([i,-1])
            
            while queue:
                index, parent = queue.popleft()
                visited[index] = 1
                
                for out_index in graph[index]:
                    if visited[out_index] == 0:
                        queue.append([out_index, index])
                    elif out_index != parent:
                        return False
        return True
        
        