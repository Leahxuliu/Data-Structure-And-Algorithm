#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/18  
# @Author  : XU Liu
# @FileName: 399.Evaluate Division.py

'''
1. 题目要求：
谷歌近6个月出了8次

2. 理解：
a/b = 2, b/c =3
相当于
a --> b --> c
  2倍    3倍
so a --> c 是6倍

a <-- b <-- c
  1/2倍   1/3倍

如果除数或者被除数不存在 --> -1.0
自己除自己 --> 1.0

3. 题目类型：
有向图，路径

4. 输出输入以及边界条件：
input: equations: List[List[str]], values: List[float], queries: List[List[str]]
output: values: List[float]
corner case: None

5. 解题思路
    1. 重点，make graph（dict里面是dict）比如{'a':'b':2.0} 表示a指向b，a/b=2.0

'''


# 提问 if not equations or equations == [[]]:
# 有区别吗


from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations, values, queries):
        if equations == None:
            return []
        
        graph = defaultdict(dict)
        for (x,y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0/val
        print(graph)
        res = []
        for i,j in queries:
            if i not in graph or j not in graph:
                res.append(-1.0)
            else:
                if i == j:
                    res.append(1.0)
                else:
                    res.append(self.count(graph, i, j))
        return res
        
    def count(self, graph, i, j):
        queue = deque()
        visited = set()
        queue.append([i, 1.0])
        
        while queue:
            node, multi = queue.popleft()
            if node == j:
                return multi
                
            visited.add(node)
            for elem in graph[node]:
                if elem not in visited:
                    #multi = multi * graph[node][elem]  
                    # 易错点 相乘不能写在这！每一个点对应一个相乘结果，如果写在这，就是累计了！！！ 注意注意！！！
                    queue.append([elem, multi * graph[node][elem]])
        return -1.0  # 不能不写！ 因为可能存在好几个群

x = Solution()
print(x.calcEquation([['x1','x2'],['x2','x3'],['x3','x4'],['x4','x5']],[3.0,4.0,5.0,6.0],[['x2','x4']]))



from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i, (a, b) in enumerate(equations):
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]
        
        def count(a, b):
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            if a in visited:
                return -1.0
                   
            visited.add(a)
            for i in graph[a]:
                val = count(i, b)
                if val != -1.0:
                    return val * graph[a][i]
            return -1.0
        
        res = []
        for a, b in queries:
            visited = set()
            res.append(count(a, b))
        return res