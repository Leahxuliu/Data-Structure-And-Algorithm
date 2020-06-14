# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/09  

'''
注意时间复杂度
for i in list, O(n)
for i in ser, O(1)

这一题如果用dict来储存info，在查找的时候，时间复杂度要大于list
'''


'''
greedy
从距离最小的bike和worker开始选

时间复杂度：O(NM)
空间复杂度：O(NM)
'''
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        if workers == [] or workers == [[]]:
            return []

        info = []
        m = len(workers)
        n = len(bikes)
        for i in range(m):
            for j in range(n):
                dis = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                info.append([dis, i, j])

        res = [-1] * len(workers)
        used = set()

        sort = sorted(info, key = lambda x:x[0])
        for dis, w, b in sort:
            if b not in used and res[w] == -1:
                res[w] = b
                used.add(b)

        return res


'''
Greedy + heap
1. 记录每一个worker与bike的距离
2. 以每一个worker为基准，找到每一个worker对应的最近的bike，记录到heap list
3. 把heap list放入heap
4. heappop最小距离
    如果该最小距离的bike还没有被用，则ok
    else，heappush这个worker对应的次小距离的bike

Time: O(nlogm)
Space: O(n)

'''
from heapq import *
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        if len(workers) == 0:
            return 0

        m = len(workers)
        n = len(bikes)
        info = [[] for _ in range(m)]

        for i, (x1, y1) in enumerate(workers):
            for j, (x2, y2) in enumerate(bikes):
                dis = abs(x1 - x2) + abs(y1 - y2)
                info[i].append([dis, i, j])

            info[i].sort(reverse = True)

        heap = [x.pop() for x in info]
        heapify(heap)
        res = [-1] * m
        used = set()
        count = 0

        while count < m:
            dist, i, j = heappop(heap)
            if res[i] == -1 and j not in used:
                res[i] = j
                used.add(j)
                count += 1
            else:
                heappush(heap, info[i].pop())
        return res
