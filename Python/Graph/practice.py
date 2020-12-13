from collections import deque, defaultdict

class Graph:
    def DFS_Traversal(self, nums, pairs):
        def dfs(node):
            if visited[node] == 1:
                return 
            
            preorder.append(node)
            visited[node] = 1
            for out in adjacent[node]:
                dfs(out)

            postorder.append(node)
            return 

        if nums == 0 or pairs == []:
            return
        
        visited = [0] * nums
        adjacent = [[] for _ in range(nums)]

        for i, j in pairs:
            adjacent[i].append(j)
            adjacent[j].append(i)

        preorder = []
        postorder = []
        for i in range(nums):
            if visited[i] == 0:
                dfs(i)
        
        print(preorder)
        print(postorder)
        return 
    
    
    def BFS_Traversal(self, nums, pairs):
        # corner case
        if nums == 0 or pairs == []:
            return
        
        visited = [0] * nums
        adjacent = [[] for _ in range(nums)]
        for i, j in pairs:
            adjacent[i].append(j)
            adjacent[j].append(i)

        order = []
        queue = deque()
        for i in range(nums):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1  # 切记，append之后立刻visited变成1

                while queue:
                    node = queue.popleft()
                    order.append(node)

                    for out in adjacent[node]:
                        if visited[out] == 0:
                            queue.append(out)
                            visited[out] = 1
        print(order)
        return 

    def Prim_findMST(self, n, edges):
        adj = defaultdict(dict)
        for i, j, w in edges:
            adj[i][j] = w
            adj[j][i] = w
        
        count = 0
        res = {}
        dist = {node: float('inf') for node in range(n)}
        dist[0] = 0

        while dist:
            i, w = sorted(dist.items(), key = lambda x:x[1])[0]
            dist.pop(i)

            res[i] = w
            count += w

            for j in adj[i]:
                if j not in res:
                    dist[j] = min(dist[j], adj[i][j])
        
        return count



x = Graph()
x.DFS_Traversal(5, [[0,1], [0,2], [0,3], [1,4]])
x.BFS_Traversal(5, [[0,1], [0,2], [0,3], [1,4]])
