from heapq import *
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # bulid the graph
        graph = defaultdict(dict)
        for i, j, w in times:
            graph[i][j] = w

        res = {}
        heap = [(0, K)]

        while heap:
            path, node = heappop(heap)

            if node in res:
                continue
            else:
                res[node] = path
            
            if len(res) == N:
                break
            
            for j in graph[node]:
                if j not in res:
                    heappush(heap, (path + graph[node][j], j))

        sortPath = sorted(res.values())
        return sortPath[-1] if len(res) == N else -1


'''
use Dijkstra
key: 1. find all shortest paths from source node to other node
2. then find the max time in 1

1. make adjacent list in dictionary
    dict[dict]
    key1: start node; key2: end node; value: weight
2. initalize a dict to store the dist from source to the node (dist)
    key: each node; value: inf; (source node 0)
3. pop the shortest time(t) in the dict, and then traverse the neighbor(j node) of popped node, change the time of j node in dict, the new dist is min(dist[j], t + w)
4. max(all shortest paths) 
'''

from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # adjancent list
        adj = defaultdict(dict)
        for i, j, w in times:
            adj[i][j] = w
        
        # init a dist
        dist = {node: float('inf') for node in range(1, N + 1)}
        dist[K] = 0

        # find the shortest paths 
        res = {}
        while dist:
            i, w = sorted(dist.items(), key = lambda x:x[1])[0]
            res[i] = w
            dist.pop(i)

            for j in adj[i]:
                if j not in res:
                    dist[j] = min(dist[j], w + adj[i][j])
        res = sorted(res.values(), key = lambda x:x)[-1]
        return res if res != float('inf') else -1
