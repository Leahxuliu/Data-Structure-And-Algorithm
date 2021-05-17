from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        heap = [1]
        res = 0
        for i in range(n):
            res = heappop(heap)
            
            while heap and heap[0] == res:
                heappop(heap)

            for j in [2, 3, 5]:
                heappush(heap, res * j)
        return res