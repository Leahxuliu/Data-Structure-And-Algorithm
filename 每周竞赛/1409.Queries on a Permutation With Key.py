#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/12  
# @Author  : XU Liu
# @FileName: 1409.Queries on a Permutation With Key.py


'''
关键点：

l.index()
l.remove()

'''
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        if queries == []:
            return []
        
        n = len(queries)
        p = [i for i in range(1, m + 1)]
        res = []
        
        for i in range(n):
            posi = p.index(queries[i])
            res.append(posi)
            val = p[posi]
            p.remove(val)
            p = [val] + p
        return res