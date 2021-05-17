'''
LC51
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        if n == 1:
            return [["Q"]]
        
        def find(col, path):
            if col == n:
                res.append(path[:])
                return

            for i in range(n):
                if i in row or col + i in dia1 or col - i in dia2:
                    continue
                row.add(i) 
                dia1.add(col + i)
                dia2.add(col - i)

                new_col = '.' * i + 'Q' + '.' * (n - 1 - i)

                find(col + 1, path + [new_col])
                row.remove(i)
                dia1.remove(col + i)
                dia2.remove(col - i)
            return 

        res = []
        # 记录已经放过皇后的row
        row = set()
        # y + x = b,记录b,也就是这个对角钱上放置过皇后
        dia1 = set()
        # y - x = b, 记录b
        dia2 = set()

        # 不需要记录column是因为，每一层要放一个皇后，递归里面按层遍历
        find(0, [])
        return res


'''
LC52
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        def find(col):
            if col == n:
                self.res += 1
                return 

            for i in range(n):
                if i in row or col + i in dia1 or col - i in dia2:
                    continue

                row.add(i)
                dia1.add(col + i)
                dia2.add(col - i)
                find(col + 1)
                row.remove(i)
                dia1.remove(col + i)
                dia2.remove(col - i)

            return 
        

        row = set()
        dia1 = set()
        dia2 = set()


        self.res = 0
        find(0)
        return self.res