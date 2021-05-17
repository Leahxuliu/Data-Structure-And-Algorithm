'''
heap
maintain a heap with k size, each time return heap[0]
'''
from heapq import heappush, heappushpop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for i in nums:
            if len(self.heap) < k:
                heappush(self.heap, i)
            else:
                heappushpop(self.heap, i)


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)