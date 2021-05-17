# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05  
# @Author  : XU Liu
# @FileName: 347.Top K Frequent Elements.py

'''
1. 题目要求：
找出现频率最多的k个数
time complexity must be better than O(n log n)

2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''

'''
dict + sort
字典排序时间复杂度O(n log n)
这里的n是key的个数
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        info = {}
        for i in nums:
            if i in info:
                info[i] += 1
            else:
                info[i] = 1

        res = sorted(info, key = lambda x:info[x], reverse = True)
        return res[:k]

'''from collections import defaultdict
    dic = defaultdict(int)
    for elem in nums:
        dic[elem] += 1'''

'''
dict + heap
O(Nlogk)
'''

# 347. Top K Frequent Elements 
from collections import defaultdict
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        info = defaultdict(int)
        for i in nums:
            info[i] += 1
            
        heap = []
        res = []
        for key, value in info.items():
            heappush(heap, (-value, key))

        while k:
            res.append(heappop(heap)[1])
            k -= 1
        return res

# 维持一个k大的heap
# 最大值用最小堆，最小值用最大堆
from collections import defaultdict
from heapq import heappop, heappush, heappushpop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        
        count = defaultdict(int)
        for i in nums:
            count[i] += 1

        # sorted_count = sorted(count.items(), key = lambda x:-x[1])

        heap = []
        for key, value in count.items():
            if len(heap) < k:
                heappush(heap, [value, key])
            else:
                heappushpop(heap, [value, key])
        
        return [each for times, each in heap]


'''
手动实现最小堆
'''

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        def heappush(heap, value, key):
            heap.append((value, key))

            i = len(heap) - 1
            while i // 2 > 0:
                if heap[i][0] < heap[i // 2][0]:
                    heap[i], heap[i // 2] = heap[i // 2], heap[i]
                    i = i // 2
                else:
                    break
            return 
        
        def heappoppush(heap, value, key):
            if heap[1][0] > value:
                return 
            
            heap[1] = (value, key)
            i = 1
            n = len(heap)
            while 2 * i < n:
                child = 2 * i 
                if child + 1 < n and heap[child + 1][0] < heap[child][0]:
                    child += 1
                if heap[child][0] < heap[i][0]:
                    heap[child], heap[i] = heap[i], heap[child]
                    i = child
                else:
                    break
            return 


        heap = [0]  # min-heap
        for key, value in count.items():
            if len(heap) - 1 < k:
                heappush(heap, value, key)
            else:
                heappoppush(heap, value, key)
        
        return [each for times, each in heap[1:]]
        

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        
        info = defaultdict(int)
        for i in nums:
            info[i] += 1


        def rasie_up(heap):
            i = len(heap) - 1
            while i > 0:
                root = i // 2
                if heap[root][0] > heap[i][0]:
                    heap[root], heap[i] = heap[i], heap[root]
                    i = root
                else:
                    break
            return 
        
        def sink_down(heap):
            end = len(heap) - 1
            i = 0
            while i * 2 <= end:
                child = i * 2
                if child + 1 <= end and heap[child + 1] < heap[child]:
                    child += 1
                if heap[child] < heap[i]:
                    heap[i], heap[child] = heap[child], heap[i]
                    i = child
                else:
                    break 
            return 
        
        # print(info)
        heap = []
        for num, times in info.items():
            if len(heap) < k:
                heap.append([times, num])
                rasie_up(heap)
            else:
                if times < heap[0][0]:
                    continue
                else:
                    heap[0] = [times, num]
                    sink_down(heap)

        # print(heap)
        return [each for times, each in heap]