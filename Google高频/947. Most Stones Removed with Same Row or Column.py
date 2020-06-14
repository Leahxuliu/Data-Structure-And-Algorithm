# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/11


'''
一次move操作可以移掉一个石头，但是这个move操作有一个要求，那就是，如果想要move某个石子，那么这个石子的行或列上必须有其他的石子。
假设有两个石子在同一行，显然第一次move操作是可以的，之后还剩下一个石子，这个石子就不能move操作，因为在它的行和列上它都是独生子女。 题目要我们求最大的move操作次数，也就是符合上述要求可以拿掉多少石子。

大佬
https://www.jianshu.com/p/30d2058db7f7
'''

# dfs
from collections import defaultdict


class Solution(object):
    def removeStones(self, stones):
        if len(stones) <= 1:
            return 0

        rows = defaultdict(set)
        columns = defaultdict(set)
        for i, j in stones:
            rows[i].add(j)
            columns[j].add(i)

        def dfs_r(i):
            seeR.add(i)
            for out in rows[i]:
                if out not in seeC:
                    dfs_c(out)
            return

        def dfs_c(i):
            seeC.add(i)
            for out in columns[i]:
                if out not in seeR:
                    dfs_r(out)
            return

        seeR = set()
        seeC = set()
        island = 0

        for i, j in stones:
            if i not in seeR:
                dfs_r(i)
                dfs_c(j)
                island += 1
        return len(stones) - island


# dfs + 优化行列处理
# 行的index:0～N - 1，列的index:N～2N-1


class Solution(object):
    def removeStones(self, stones):
        if len(stones) <= 1:
            return 0

        info = defaultdict(set)
        for i, j in stones:
            info[i].add(j + 10000)
            info[j + 10000].add(i)

        def dfs(i):
            # if i in visited:
            #    return
            visited.add(i)
            for out in info[i]:
                if out not in visited:
                    dfs(out)
            return

        visited = set()
        island = 0
        for i, j in stones:
            if i not in visited:
                dfs(i)
                dfs(j + 10000)
                island += 1
        return len(stones) - island


# union find
class Solution(object):
    def removeStones(self, stones):
        if len(stones) <= 1:
            return 0

        def find(i):
            if i == gT[i]:
                return i
            return find(gT[i])

        gT = {}
        for i, j in stones:
            j = j+10000
            gT.setdefault(i, i)
            gT.setdefault(j, j)

            root1 = find(i)
            root2 = find(j)

            if root1 != root2:
                gT[root2] = root1
        return len(stones) - len({find(x) for x in gT})


# 格式化 shift + option + F