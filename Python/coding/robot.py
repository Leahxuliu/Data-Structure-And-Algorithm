'''
BFS + Memo
1. use memo to store how many steps from start to maze[i][j]
2. use BFS to scan the maze
'''

from collections import deque

def shortestDistance(maze, start, destination):
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    m = len(maze)
    n = len(maze[0])

    memo = [[float('inf')] * n for _ in range(m)]
    memo[start[0]][start[1]] = 0
    #visited = set()

    queue = deque()
    queue.append(start)
    #visited.add((start[0], start[1]))

    while queue:
        i, j = queue.popleft()

        for dx, dy in directions:
            x = i + dx
            y = j + dy
            step = memo[i][j]
            while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                x = x + dx
                y = y + dy
                step += 1
            
            x -= dx
            y -= dy

            if memo[x][y] > step:
                queue.append([x, y])
                #visited.add((x, y))
                memo[x][y] = step


    print(memo)
    if memo[destination[0]][destination[1]] == float("inf"):
        return -1
    else:
        return memo[destination[0]][destination[1]]


maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]

print(shortestDistance(maze, start, destination))

