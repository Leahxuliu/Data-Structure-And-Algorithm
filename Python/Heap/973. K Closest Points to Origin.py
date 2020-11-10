# list + sort
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pointInfo = []
        for x, y in points:
            pointInfo.append([x * x + y * y, x, y])
        
        sort = sorted(pointInfo, key = lambda x:x[0])
        res = []

        for i in range(K):
            res.append(sort[i][1:])
        
        return res


# dict + heap
from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pointInfo = {}
        for x, y in points:
            pointInfo[(x, y)] = x * x + y * y
                
        return nsmallest(K, pointInfo, key = lambda x: pointInfo[x])