'''
Trie + DFS

用Trie来储存words
遍历board
找到的words在Trie里面删掉，防止重复出现
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]: 
        n = len(board)
        m = len(board[0])

        root = {}

        for w in words:
            curr = root
            for c in w:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['Finish'] = w
        # print(root)
        
        def dfs(i, j, root):
            if i < 0 or j< 0 or i >= len(board) or j >= len(board[0]):
                return 

            root = root[board[i][j]]  # 一定要先写
            if 'Finish' in root:
                res.append(root['Finish'])
                root.pop('Finish')
                # return 不一定结束 比如eati，eat

            visited[i][j] = 1
            for (x, y) in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1,j)]:
                if x >= 0 and y >= 0 and x < len(board) and y < len(board[0]):
                    if visited[x][y] == 0 and board[x][y] in root:
                        dfs(x, y, root)
            visited[i][j] = 0
            return 
        
        res = []
        visited = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] in root:
                    dfs(i, j, root)
        return res






# 超时
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if board == [] or board == [[]]:
            return []
        
        def find(i, j, path, target):
            
            if path == target:
                res.add(path)
                return
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return 
            if visited[i][j] == 1:
                return 
            
            visited[i][j] = 1
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                find(x, y, path + board[i][j], target)
            visited[i][j] = 0
            
            return
        
        
        start_chars = set()
        for i in range(len(words)):
            start_chars.add(words[i][0])

        words = words
        res = set()
        visited = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                for target in words:
                    if target not in res and board[i][j] == target[0]:
                            find(i, j, '', target)
        return list(res)