from collections import deque, defaultdict
class Solution:
    def validTree(self, n, edges) -> bool:
        if not n:
            return False
        if n == 1:
            return True
        if not edges:
            return False
        if n != len(edges) + 1:
            return False

        visited = [0] * n
        graph = defaultdict(set)
        queue = deque()
        
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
            
        for i in range(n):
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

x = Solution()
print(x.validTree(5,[[1,2],[0,3],[4,3],[0,4]]))