'''
215. Kth Largest Element in an Array
'''

from heapq import heapify, heappush, heappushpop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)

        for i in range(k):
            heappush(heap, nums[i])

        for i in range(k, n):
            heappushpop(heap, nums[i])
        
        return heappop(heap)

    