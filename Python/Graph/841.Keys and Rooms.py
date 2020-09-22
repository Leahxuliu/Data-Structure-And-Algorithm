#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/16  
# @Author  : XU Liu
# @FileName: 841. Keys and Rooms.py

'''
1. 题目要求：


2. 理解：
只有一个群 --> true
多个群 --> False （会有room进不去）
注意，给到的list不是单纯的邻接表，里面包括理解的room钥匙以及自己room的钥匙 --> 不重要

3. 题目类型：
有向图

4. 输出输入以及边界条件：
input: list
output: T/F
corner case: None --> T

5. 解题思路
    1. 用dfs遍历或者bfs
    2. 遍历过的点记录到visited里面
'''

'''
错误
[[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]]
0，1，2，3，4，5，7和6，8，9是两个组
但是visited都是1
需要改进点：只能在一个环里面遍历
从0开始为起点
'''
class Graph:
    def canVisitAllRooms(self, rooms):
        if rooms == None:
            return True
        if len(rooms) == 1:
            return True
         
        visited = [0] * len(rooms)   
        
        def dfs(index):
            for each_key in rooms[index]:
                if each_key != index:
                    if visited[each_key] == 1:
                        return
                    visited[each_key] = 1
                    dfs(each_key)
            return
            
        for index in range(len(rooms)):  # 错误点在此，从0为起点开始遍历，只遍历包含0的那个环
            if index == 0:
                dfs(index)
                visited[index] = 1
            else:
                if visited[index] == 0:
                    dfs(index)
        print(visited)
        return visited == [1] * len(rooms)



'''
正确答案
以0为起点开始遍历
'''
class Graph:
    def canVisitAllRooms(self, rooms):
        if rooms == None:
            return True
        if len(rooms) == 1:
            return True
         
        visited = [0] * len(rooms)   
        
        def dfs(index):
            if visited[index] == 1:
                return

            visited[index] = 1
            
            for each_key in rooms[index]:
                dfs(each_key)
            return
            
        visited[0] = 1  
        for index in rooms[0]:        
            if visited[index] == 0:
                dfs(index)
        
        return visited == [1] * len(rooms)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms == [[]] or rooms == [] or len(rooms) == 1:
            return True
        
        visited = [0] * len(rooms)
        def dfs(index):
            if visited[index] == 1:
                return 
            visited[index] = 1
            for each_key in rooms[index]:
                if visited[each_key] != 1:
                    dfs(each_key)
            
        island_numb = 0
        for i, v in enumerate(visited):
            if v == 0:
                dfs(i)
                island_numb += 1
        return island_numb == 1


'''
方法2
bfs
Time Complexity: O(N + E)O(N+E), where NN is the number of rooms, and EE is the total number of keys.
Space Complexity: O(N)O(N) in additional space complexity, to store stack and seen.
'''

from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms == None:
            return True
        if len(rooms) == 1:
            return True
        
        visited = [0] * len(rooms)
        
        queue = deque()
        queue.append(0)
        
        while queue:
            index = queue.popleft()
            
            if visited[index] == 0:
                visited[index] = 1
                for i in rooms[index]:
                    if visited[i] == 0:
                        queue.append(i)
        return visited == [1] * len(rooms)


from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if rooms == [] or rooms == [[]] or len(rooms) == 1:
            return True
        
        visited = [0] * len(rooms)
        
        queue = deque()
        island_num = 0
        for i, v in enumerate(visited):
            if v == 0:
                queue.append(i)
                island_num += 1
                
                while queue:
                    index = queue.popleft()
                    visited[index] = 1
                    for out in rooms[index]:
                        if visited[out] != 1:
                            queue.append(out)
        return island_num == 1
        

x = Graph()
print(x.canVisitAllRooms([[1],[2],[3],[]]))