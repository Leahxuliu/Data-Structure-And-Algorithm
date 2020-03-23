#!/usr/bin/python
# -*- coding: utf-8 -*-

# union find的升级版

class Graph:
    def unionFind(self, n, pairs):
        if not pairs or pairs == [[]]:
            return None
        
        groupTag = [i for i in range(n)]
        rank = [1] * n  # 用一个rank来记录该node下面有几个相关node

        def find(index):
            if groupTag[index] == index:
                return index
            else:
                return find(groupTag[index])

        connect = 0
        for i, j in pairs:
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                if rank[root1] >= rank[root2]:
                    rank[root1] += rank[root2]
                    groupTag[root2] == root1
                    connect += 1
                else:
                    rank[root2] += rank[root1]
                    groupTag[root1] = root2
                    connect += 1
        
        return (n - connect)
        
x = Graph()
print(x.unionFind(6, [[0,1], [1,2], [3,4], [5,3], [1,3]]))