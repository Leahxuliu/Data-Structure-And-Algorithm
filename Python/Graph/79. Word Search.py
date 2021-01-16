'''
1. DFS to traversal the graph
2. find each of character in word

'''
from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traversal(i, j, target):
            '''
            return True or False
            '''
            if target > len(word) - 1:
                return False
            if i > len(board) - 1 or i < 0:
                return False
            if j > len(board[0]) - 1 or j < 0:
                return False
            if visited[i][j] == 1:
                return False
            if word[target] != board[i][j]:
                #visited[i][j] = 0
                return False
            if target == len(word) - 1 and word[target] == board[i][j]:
                return True

            #print(i, j, target, word[target], board[i][j])
            visited[i][j] = 1
            target += 1
            for (x, y) in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
                if traversal(x, y, target) == True:
                    return True
            visited[i][j] = 0
            return False
            
        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = [[0] * m for _ in range(n)]
                    #print('a')
                    if traversal(i, j, 0):
                        return True
        return False