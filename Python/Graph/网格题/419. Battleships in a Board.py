'''
1. use visited list to memo visited nodes
2. traversal(BFS) the nodes and count how many the components in board

'''
from collections import deque
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if board == [] or board == [[]]:
            return 0
        
        n = len(board)
        m = len(board[0])

        visited = [[0] * m for _ in range(n)]
        count = 0

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' and visited[i][j] == 0:
                    queue = deque()
                    queue.append([i, j])
                    visited[i][j] = 1 
                    count += 1

                    while queue:
                        x, y = queue.popleft()
                        for (x2, y2) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                            if x2 >= 0 and x2 < n and y2 >= 0 and y2 < m:
                                if visited[x2][y2] == 0 and board[x2][y2] == 'X':
                                    queue.append([x2, y2])
                                    visited[x2][y2] = 1
        return count


'''
count the start of ships

1. traversal board from left to right, top to bottom
2. if board[i][j] is 'X', count
    but, if board[i][j - 1] is 'X' or board[i - 1][j] is 'X', not count
'''

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if board == [] or board == [[]]:
            return 0

        count = 0
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    if board[i][j] == 'X':
                        count += 1
                elif i == 0:
                    if board[i][j] == 'X' and board[i][j - 1] != 'X':
                        count += 1
                elif j == 0:
                    if board[i][j] == 'X' and board[i - 1][j] != 'X':
                        count += 1
                else:
                    if board[i][j] == 'X' and board[i - 1][j] != 'X' and board[i][j - 1] != 'X':
                        count += 1
        return count