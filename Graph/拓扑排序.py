#!/usr/bin/python
# -*- coding: utf-8 -*-

# 拓扑排序
# topological sort method 
from collections import deque
class mySolution:
    def topoSort(self, num, prerequisities):  # num: 节点数量；prerequisities(先决条件): [[0, 1], [],...] 依赖关系, 1-->0 (0依赖1)
        outdegree = [[] for _ in range(num)]  # 所有节点的空出度表，包含出度的点的index，即邻接表
        indegree = [0 for _ in range(num)]  # 所有节点的空入度表，包含入度点的数量
        # 或者 indegree = [0] * num
        # 但是不能 outdegree = [[]] * num!

        for x, y in prerequisities:  # 通过依赖关系去填充入度和出度表
            outdegree[y].append(x)  #  填充出度表
            indegree[x] += 1  # 填充入度表
        print(outdegree)
        print(indegree)
        
        queue = deque()
        for i, each_in in enumerate(indegree):  # 把所有入度为0的点的序号加入queue
            if each_in == 0:
                queue.append(i)
        # 可以合并成
        # queue = deque([i for i, v in enumerate(indegree) if v == 0])
        
        while queue:
            node_index = queue.popleft()  # popleft每个元素
            for out_ind in outdegree[node_index]:  # 遍历其所有出度点
                indegree[out_ind] -= 1 # 出度点的入度 - 1
                if indegree[out_ind] == 0:  # 若出度点的入度为0，queue append该出度点
                    queue.append(out_ind)
        
        if indegree == [0] * num:
            return '无环'
        else:
            return '有环'
x = mySolution()
print(x.topoSort(5, [[0,1], [0,2], [0,3], [1,4]]))