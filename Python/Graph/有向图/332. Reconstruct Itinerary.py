'''
保存边
'''
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if tickets == [] or tickets == [[]]:
            return 
        
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        
        for k, v in graph.items():
            v.sort()

        def traversal(node, path):
            # 这里不能是if len(path) == len(tickets) + 1:
            # 因为最后一个node的时候，graph里面没有内容了，不会再次进行dfs
            # 特别容易错
            if len(path) == len(tickets):
                self.res = path[:] + [node]
                return 
            
            path.append(node)
            for _ in graph[node]:
                out = graph[node].pop(0)
                traversal(out, path)
                if self.res:
                    return 
                graph[node].append(out)

            path.pop()
            return 

        self.res = []
        traversal('JFK', [])
        return self.res
            


        

