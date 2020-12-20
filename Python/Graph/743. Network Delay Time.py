# 基本模型
# 先把所有点都加入到dict里
# 每次pop最近的一个点
# 以点为基准
# from CS61B

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
        res = max(res.values())
        return res if res != float('inf') else -1