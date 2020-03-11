#!/usr/bin/python
# -*- coding: utf-8 -*-

class MySolution:
    def dfsGraph(self, num, slides):
        graph = [[] for _ in range(num)]  # 建立空邻接表 tO(N)
        visited = [0 for _ in range(num)]  # 建立空访问表

        for i, j in slides:  # 填充邻接表 tO(E)
            graph[i].append(j)
            graph[j].append(i)

        index = 0
        

        self.DFS(index, graph, visited)  # case1, 所有节点都连在一起时的遍历方法，从第0个节点开始访问
        
#         for ind, neighbor in enumerate(graph):  # case1, 并不是所有节点都连在一起时的遍历方法，从第0个节点开始访问
#             if visit[ind] == 0:  # 不遍历已经访问的节点，（根据实际情况，可以删除）
#                 self.DFS(index, graph, visited)
        return

    def DFS(self, index, graph, visited):  # 访问
        if visited == [1] * len(visited):  # end condition
            return

        print('node index is %s' % index)
        visited[index] = 1  # 表示已访问该点 tO(1)
        print(visited)

        for node_ind in graph[index]:  # 遍历第index节点的邻接行里的邻接节点
            if visited[node_ind] == 0:  # 若邻接节点未被访问过
                self.DFS(node_ind, graph, visited)
        
x = MySolution()
x.dfsGraph(5, [[0,1], [0,2], [0,3], [1,4]])