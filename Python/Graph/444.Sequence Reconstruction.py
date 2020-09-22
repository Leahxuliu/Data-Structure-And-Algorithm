#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/19  
# @Author  : XU Liu
# @FileName: 444.Sequence Reconstruction.py

'''
1. 题目要求：


2. 理解：
seq能否重构成org，且org是唯一重构的结果

3. 题目类型：
有向图路径

4. 输出输入以及边界条件：
input: org: List[int], seqs: List[List[int]]
output: bool
corner case: seq = None

5. 解题思路
    1. 把seq组成一个整体的有向图 先写成pair，再组合成graph
    2. 找路径
    3. 看org是不是唯一一个包含所有node的路径
    4. 如果是个环，肯定不是唯一org

    易错点：node是从1开始的，不是从0开始

'''


'''
错误
因为这样的话，只有一个path，没有考虑有多个path的情况
[-1,0,1] 只能循环一次，不能考虑到所有的path？？？
另外 n可以= 10 ^ 4。有了那么大的n和偏斜的树测试用例，递归深度就很容易超过
'''
'''
class Solution:
    def sequenceReconstruction(self, org, seqs) -> bool:
        if seqs == None:
            return False
        
        pair = []
        nodes = set()
        
        for each_seq in seqs:
            if len(each_seq) == 1:
                nodes.add(each_seq[0]-1)
            else:
                for i, s in enumerate(each_seq):
                    if i < len(each_seq) - 1:
                        if [s-1, each_seq[i+1]-1] not in pair:
                            pair.append([s-1, each_seq[i+1]-1])
                            nodes.add(s-1)
                            nodes.add(each_seq[i+1]-1)

        graph = [[] for _ in range(len(nodes))]
        visited = [-1] * len(nodes)
        
        for i,j in pair:
            graph[i].append(j)

        path = []
        for i in range(len(nodes)):
            if self.pathDFS(graph, visited, i, path) == True:
                return False

        path = [i+1 for i in path]
        print(path)
        if path == org[::-1]:
            return True
        else:
            return False
        
    def pathDFS(self, graph, visited, index, path):
        if visited[index] == 0:
            return True
        if visited[index] == 1:
            return False
        
        visited[index] = 0
        for elem in graph[index]:
            if self.pathDFS(graph, visited, elem, path) == True:
                return True
        
        visited[index] = 1
        path.append(index)
        
        return False
'''        

'''
from 李厨子
用拓扑排序
出度和入度都用dict来表示，因为node的起点不是0
two 0 indegree node说明可以有两种seq --> False ??? why???
出度有两种可能时，说明不是唯一的seq --> 不一定，比如 [1,2,3]  [[1,2],[1,3],[2,3]]
'''

from collections import defaultdict, deque
class Solution:
    def sequenceReconstruction(self, org, seqs) -> bool:
        if not seqs:
            return False
        
        indegree = defaultdict(int)
        outdegree = defaultdict(list)
        nodes = set()

        for each_seq in seqs:
            for s in each_seq:
                indegree[s] = 0
                nodes.add(s)

        for each_seq in seqs:
            for i in range(len(each_seq)-1):
                indegree[each_seq[i+1]] += 1
                outdegree[each_seq[i]].append(each_seq[i+1])
        
        if set(org) != nodes:  # set是按顺序加入的 # 注意这个corner case， seq里面的elem不存在于org
            return False

        queue = deque()
        all_path = []
        for k, v in indegree.items():
            if v == 0:
                queue.append([k,[]])
        
        if len(queue) > 1:
            return False
        
        while queue:
            index, path = queue.popleft()
            path.append(index)
            
            if index not in outdegree:
                all_path.append(path)
                break
                
            for out_index in outdegree[index]:
                indegree[out_index] -= 1
                if indegree[out_index] == 0:
                    queue.append([out_index, path])
        print(all_path)
        if org in all_path:
            return True
        else:
            return False
    

x = Solution()
print(x.sequenceReconstruction([1],[[1],[2,3],[3,2]]))

