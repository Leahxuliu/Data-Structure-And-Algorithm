#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/19  
# @Author  : XU Liu
# @FileName: 733.Flood Fill.py

'''
1. 题目要求：


2. 理解：
用list表示行列-->表示地图
跟开始点颜色相同的点会被染色
从指定的开始点开始，一次循环，所以不需要visited

3. 题目类型：
网格搜索

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 解题思路
    1. DFS或者BFS的网格搜索
易错点：开始颜色不一定是1

'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return []
        
        startColor = image[sr][sc]
        
        def dfs(i, j):
            if i < 0 or j < 0 or i > len(image) - 1 or j > len(image[i]) - 1 or image[i][j] != startColor or image[i][j] == newColor:  # 千万不能忘记写image[i][j] == newColor，不然会一直在里面循环
                return image
            
            image[i][j] = newColor
            dfs(i - 1, j)  
            dfs(i + 1, j)  
            dfs(i, j - 1)  
            dfs(i, j + 1)  
            return image
            
        dfs(sr, sc)
        return image

class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        if image[sr][sc] == newColor:  # corner case
            return image

        color = image[sr][sc]
        from collections import deque
        queue = deque([(sr, sc)])
        image[sr][sc] = newColor

        while queue:
            r, c = queue.popleft()
            if r - 1 >= 0 and image[r - 1][c] == color:
                queue.append([r - 1, c])
                image[r - 1][c] = newColor
            if r + 1 <= len(image) - 1 and image[r + 1][c] == color:
                queue.append([r + 1, c])
                image[r + 1][c] = newColor
            if c - 1 >= 0 and image[r][c - 1] == color:
                queue.append([r, c - 1])
                image[r][c - 1] = newColor
            if c + 1 <= len(image[0]) - 1 and image[r][c + 1] == color:
                queue.append([r, c + 1])
                image[r][c + 1] = newColor
        return image



from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image == None:
            return []
        
        startColor = image[sr][sc]
        
        queue = deque()
        queue.append([sr,sc])
        
        while queue:
            i,j =  queue.popleft()
            image[i][j] = newColor
            
            if i-1 >= 0 and image[i-1][j] == startColor and image[i-1][j] != newColor:
                queue.append([i-1, j])
            if i + 1 <= len(image) - 1 and image[i+1][j] == startColor and image[i+1][j] != newColor:
                queue.append([i+1, j])
            if j -1 >= 0 and image[i][j-1] == startColor and image[i][j-1] != newColor:
                queue.append([i, j-1])
            if j + 1 <= len(image[i]) -1 and image[i][j+1] == startColor and image[i][j+1] != newColor:
                queue.append([i,j+1])
        return image