# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/02  
# @Author  : XU Liu
# @FileName: 215.Kth Largest Element in an Array.py

'''
1. 题目要求：


2. 理解：
sort list的话, O(NlogN)
用heap进行优化

3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''

'''
直接sort
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

'''
用heap

以用最小堆找最大kth值:
    1. 建立一个k大小的最小堆, heapify(arr[:k])
    2. 加arr[k]到heap中，删掉最小值(先加后删 heappushpop)
    3. 重复上一步,直到arr里的值都被加入到heap (arr[k:])
    4. pop出来的便是最后的答案
T: O(Nlogk) k是第几大，N是元素个数
'''
from heapq import heapify, heappushpop, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for i in nums[k:]:
            heappushpop(heap, i)
        return heappop(heap)

from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heappush(heap, -i)
        while k:
            res = heappop(heap)
            k -= 1
        return -res
'''

1. Y = -X
2. 建立heap
3. heappop k次
4. 再取负值
T: O(N + klogN) k是第几大，N是元素个数
'''
from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapify(heap)
        for i in range(k):
            res = heappop(heap)
        return -res


'''
用heap方法3
T: O(nlogk) 
'''

from heapq import heapify, nlargest
class Solution:
    def findKthLargest(self, nums, k):
        heapify(nums)
        return nlargest(k, nums)[-1]