#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/16  
# @Author  : XU Liu
# @FileName: 1376.Time Needed to Inform All Employees.py

'''
1. 题目要求：


2. 理解：
一个公司有n个员工
每一个员工都有一个ID
manager[i] is the direct manager of the i-th employee
manager[headID] = -1
通知是一层传一层的
算通知事情的所需要的时间
也就是，算有几层，然后把每一层对应的时间相加

3. 题目类型：
有向图，求几层

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 解题思路
    1. bfs求深度
    2. make graph
    3. 从headID开始遍历,层层遍历

易错点：
注意同一层里有两个leader的情况！！！
'''

'''
错误
没有考虑到分群的情况
'''
'''
from collections import deque
class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        if n == 0:
            return 0
        if n == 1:
            return informTime[0]
                
        queue = deque()
        queue.append(headID)
        Time = 0
        
        while queue:
            q_len = len(queue)
            max_time = 0
            for i in range(q_len):
                head_ID = queue.popleft()
                max_time = max(max_time, informTime[head_ID])
                for empl_ID, head in enumerate(manager):
                    if head == head_ID:
                        queue.append(empl_ID)
            Time += max_time
        return Time
'''

'''
正确
类似二叉树里面，求sum path
'''
from collections import deque, defaultdict
class Solution:
    def numOfMinutes(self, n, headID, manager, informTime) -> int:
        if n == 0:
            return 0
        if n == 1:
            return informTime[0]
        
        graph = defaultdict(list)
        for i, v in enumerate(manager):  # index --> value; v --> key
            graph[v].append(i)
            
        print(graph)
        queue = deque()
        queue.append([headID, 0])
        max_time = 0
        
        while queue:
            ID, time = queue.popleft()
            time += informTime[ID]
            if ID not in graph:
                max_time = max(time, max_time)
            else:
                for elem in graph[ID]:
                    queue.append([elem, time])
        return max_time


x = Solution()
print(x.numOfMinutes(11,4,[5,9,6,10,-1,8,9,1,9,3,4],[0,213,0,253,686,170,975,0,261,309,337]))
