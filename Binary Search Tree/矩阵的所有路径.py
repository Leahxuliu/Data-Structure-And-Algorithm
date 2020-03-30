#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
2,3,4,7
3,5,7,2
1,3,4,5
4,7,8,15

求从2到15的所有path
可以往回走，但是每一个node在该path里面只能出现一次，不能走重复
'''


def dfs(i, j):
    for path, visited in all_path:
    if i < 0 or j <0 or i >= len(visited) or j >= len(visited[0]) or visited[i][j] == 1 or matrix[i][j] == matrix[len(matrix)-1][len(matrix[0])-1]:
        return

    



from collections import deque
if __name__ == "__main__":
    matrix = [[2,3,4,7],[3,5,7,2],[1,3,4,5],[4,7,8,15]]
    all_path = {}
    all_path[str(matrix[0][0])] = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    dfs(0,0)

