#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/21  
# @Author  : XU Liu
# @FileName: 547.Friend Circles.py

'''
1. 题目要求：


2. 理解：
找交际圈
易错！！！跟网格搜索注意区分
把行列抽象成无向图，找岛屿
比如M[0][1]=1 --> 0-1相连

3. 题目类型：
无向图的群个数

4. 输出输入以及边界条件：
input: 行列的list
output: int
corner case: M == None 

5. 解题思路
    

'''


'''
网格搜索
错误
因为网格搜索只能上下左右，不能斜走
可这道题，对角线一定都是1，自己跟自己是1
'''

'''
from collections import deque

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        visited = [[0] * len(M[0]) for _ in range(len(M))]
        
        queue = deque()
        circle = 0
        for i in range(len(M)):
            for j in range(len(M[i])):
                if M[i][j] == 1 and visited[i][j] == 0:
                    queue.append([i, j])
                    visited[i][j] = 1
                    
                    while queue:
                        r, c = queue.popleft()
                        if r - 1 > 0 and visited[r-1][c] == 0 and M[r-1][c] == 1:
                            queue.append([r-1,c])
                            visited[r-1,c] = 1
                        if r + 1 <= len(M) - 1 and visited[r+1][c] == 0 and M[r+1][c] == 1:
                            queue.append([r+1,c])
                            visited[r+1][c] = 1
                        if c - 1 > 0 and visited[r][c-1] == 0 and M[r][c-1] == 1:
                            queue.append([r,c-1])
                            visited[r][c-1] = 1
                        if c + 1 <= len(M[r]) - 1 and visited[r][c+1] == 0 and M[r][c+1] == 1:
                            queue.append([r,c+1])
                            visited[r][c+1] = 1
                            
                    circle += 1
        return circle
'''

'''
DFS
1. create a visited list to memo wheather the cell is visited or not
2. use a for loop to scan 0 to len(M) - 1
    a. use dft to scan the neighbor cells which has not been visited
'''

class Solution:
    def findCircleNum(self, M) -> int:
        if M == [] or M == [[]]:
            return 0
        if len(M) == 1:
            return 1
        
        visited = [0] * len(M)
        circle = 0

        def dfs(index):
            visited[index] = 1

            # for j in range(index): 错误 因为这题相当于无向图，只到index的话 相当于有向图
            for j in range(len(M)):
                if M[index][j] == 1 and visited[j] == 0:
                    dfs(j)

        
        for i in range(len(M)):
            if visited[i] == 0:
                dfs(i)
                circle += 1
        return circle


'''
BFS
'''
from collections import deque
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if M == [] or M == [[]]:
            return 0
        
        m = len(M)
        if m == 1:
            return 1
        
        visited = [0] * m
        circle = 0
        queue = deque()
        for i in range(m):
            if visited[i] == 0:
                circle += 1
                queue.append(i)
                visited[i] = 1
            while queue:
                index = queue.popleft()
                for j in range(m):  # for j in range(i+1, m) 可
                    if M[index][j] == 1 and visited[j] == 0:
                        queue.append(j)
                        visited[j] = 1
        return circle

'''
并查集
易错点：
for i in range(len(M)):
            for j in range(i+1,len(M)):

0: 1，2，3
1: 2，3
2: 3
'''

class Solution:
    def findCircleNum2(self, M) -> int:
        if M == None:
            return 0
        if len(M) == 1:
            return 1
        
        gT = [i for i in range(len(M))]
        def find(index):
            if gT[index] == index:
                return index
            else:
                return find(gT[index])  # 易错，不能忘记return
            
        times = 0    
        for i in range(len(M)):
            for j in range(i+1,len(M)):  # 易错点！
                if M[i][j] == 1:
                    root1 = find(i)
                    root2 = find(j)
                    if root1 == root2:
                        pass
                    else:
                        gT[root2] = root1
                        times += 1
        return len(M) - times



'''
union find + rank

'''

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if M == [] or M == [[]]:
            return 0
        
        m = len(M)
        if m == 1:
            return 1
        
        gT = [x for x in range(m)]
        rank = [1] * m
        times = 0
        
        def find(i):
            while i != gT[i]:
                gT[i] = gT[gT[i]]
                i = gT[i]
            return i
        '''
        def find(i):
            if i == gT[i]:
                return i
            else:
                return find(gT[gT[i]])
        
        def find(i):
            if i == gT[i]:
                return i
            else:
                gT[i] = find(gT[i])
                return gT[i]
        '''
        
        for i in range(m):
            for j in range(i+1, m):
                if M[i][j] == 1:
                    root1 = find(i)
                    root2 = find(j)
                
                    if root1 != root2:
                        if rank[i] >= rank[j]:
                            rank[i] += rank[j]
                            gT[root2] = root1
                            times += 1
                        else:
                            rank[j] += rank[i]
                            gT[root1] = root2
                            times += 1
        return m - times
x = Solution()
print(x.findCircleNum2([[1,1,1],[1,1,1],[1,1,1]]))