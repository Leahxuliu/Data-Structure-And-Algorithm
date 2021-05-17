'''
Greedy

each time pop two char in heap
'''
from heapq import heapify, heappop, heappush
from collections import defaultdict
class Solution:
    def reorganizeString(self, S: str) -> str:
        if S == '':
            return ''
        
        info = defaultdict(int)
        for i in S:
            info[i] += 1
        
        heap = [(-v, k) for k, v in info.items()]
        heapify(heap)

        res = ''
        while heap:
            if len(heap) == 1:
                if heap[0][0] < -1:
                    return ''
                else:
                    times, char = heappop(heap)
                    res += char
            else:
                temp = []
                for _ in range(2):
                    times, char = heappop(heap)
                    res += char 
                    times += 1
                    if times != 0:
                        temp.append((times, char))
                for each in temp:
                    heappush(heap, each)
        return res