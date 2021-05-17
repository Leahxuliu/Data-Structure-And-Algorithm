
'''
36
'''

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        cell = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in col[i]:
                    return False
                col[i].add(board[i][j])

                if board[i][j] in row[j]:
                    return False
                row[j].add(board[i][j])

                key = (i // 3, j // 3)
                if board[i][j] in cell[key]:
                    return False
                cell[key].add(board[i][j])
        return True