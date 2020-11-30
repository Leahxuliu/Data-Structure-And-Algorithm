# Prim dict版

from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        n = len(points)
        adj = defaultdict(dict)

        for i in range(n - 1):
            for j in range(i + 1, n):
                adj[i][j] = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
                adj[j][i] = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
        
        dist = {node: float('inf') for node in range(n)}
        dist[0] = 0
        res = {}
        count = 0

        while dist:
            i, w = sorted(dist.items(), key = lambda x:x[1])[0]
            dist.pop(i)
            
            res[i] = w
            count += w
            
            for j in adj[i]:
                if j not in res:
                    dist[j] = min(dist[j], adj[i][j])
        
        return count

# Prim heap版
from collections import defaultdict
from heapq import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        n = len(points)
        adj = defaultdict(dict)

        for i in range(n - 1):
            for j in range(i + 1, n):
                adj[i][j] = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
                adj[j][i] = abs(points[i][1] - points[j][1]) + abs(points[i][0] - points[j][0])
        
        heap = [(0, 0)]  # path, node
        res = {}
        count = 0
        
        while heap:
            w, i = heappop(heap)
            
            if i not in res:
                count += w
                res[i] = w
            
            if len(res) == n:
                break
            
            for j in adj[i]:
                if j not in res:
                    heappush(heap, (adj[i][j], j))
        
        return count


# 优化
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        count = 0

        dist = {(x, y): float('inf') for x, y in points}
        # 任意取一点作为起始点
        maked = [dist.popitem()[0]]

        while dist:
            # 已经done里面的最后一个point与剩下的point对比（也就是分成两个set）
            # 找到最短的横切边
            for point, value in dist.items():
                x, y = point
                i, j = maked[-1]
                temp = abs(x - i) + abs(y - j)
                dist[point] = min(value, temp)
            point, value = sorted(dist.items(), key = lambda x:x[1])[0]
            count += value
            dist.pop(point)
            maked.append(point)
        return count


# Kruskal
from heapq import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(v):
            while groupTag[v] != v:
                groupTag[v] = groupTag[groupTag[v]]
                v = groupTag[v]
            return v
        
        def union(root1, root2):
            if rank[root1] < rank[root2]:
                groupTag[root1] = root2
                rank[root2] += rank[root1]
            else:
                groupTag[root2] = root1
                rank[root1] += rank[root2]
        
        n = len(points)
        # make pairs
        heap = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                temp = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heap.append((temp, i, j))
        
        groupTag = {i:i for i in range(n)}
        rank = {i:1 for i in range(n)}
        count = 0
        times = 0

        heapify(heap)
        while times != n - 1:
            w, i, j = heappop(heap)
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                union(root1, root2)
                count += w
                times += 1
        return count