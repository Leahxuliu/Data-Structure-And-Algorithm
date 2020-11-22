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
