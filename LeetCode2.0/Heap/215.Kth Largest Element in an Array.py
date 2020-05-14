'''
Methon
A. Heap1
Steps:
    1. create a empty heap
    2. traverse nums, push -nums[i] into heap
    3. heappop heap k times
    4. take negative
time: O(klogN)
space: O(N)

B.Heap2
Steps:
    1. convert nums[:k] into heap
    2. traverse nums[k:] and heappushpop nums[i]
    3. heappop the min number of heap using heappop
Time: O(Nlogk)
Space:O(k)
    
'''

from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums == []:
            return 
        
        heap = []
        for i in nums:
            heappush(heap, -i)
        
        res = 0
        for _ in range(k):
            res = heappop(heap)
        
        return -res



from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums == []:
            return 
        
        heap = nums[:k]
        heapify(heap)
        
        for i in nums[k:]:
            heappushpop(heap, i)
        
        return heappop(heap)