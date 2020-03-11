#!/usr/bin/python
# -*- coding: utf-8 -*-

class MySolution:
    def dfsGraph(self, num, pairs):
        graph = [[] for _ in range(num)]  # 建立空邻接表 [[],[],[],[],[]] tO(N)
        visited = [0] * (num + 1)  # 建立空访问表
        #visited = [0 for _ in range(num)]

        for i, j in pairs:  # 填充邻接表 tO(E)
            graph[i].append(j)
            graph[j].append(i)
        print(graph)

        index = 0
        
        self.DFS(index, graph, visited)  # case1, 所有节点都连在一起时的遍历方法，从第0个节点开始访问
        return

    def DFS(self, index, graph, visited):  # 访问
        if visited == [1] * len(visited):  # endding condition; [1,1,1,1,1]全部被访问过
            return

        print('node index is %s' % index)
        visited[index] = 1  # 表示已访问该点 tO(1)
        print(visited)

        for node_index in graph[index]:  # 遍历第index节点的邻接节点
            if visited[node_index] == 0:  # 该邻接节点是否被访问过
                self.DFS(node_index, graph, visited)
        
x = MySolution()
x.dfsGraph(5, [[0,1], [0,2], [0,3], [1,4]])