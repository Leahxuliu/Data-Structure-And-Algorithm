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