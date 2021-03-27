# 回溯
# 超时
# 本质是一道数学题

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        def dfs(path, column, row):
            print(path, column, row)
            if len(path) == sum(destination):
                
                self.allRes += 1
                if self.allRes == k:
                    self.res = ''.join(path)
                    #print(self.res)
                    return
            
            for i in range(column, destination[1]):
                #path.append('H')
                dfs(path + ['H'], i + 1, row)
                #path.pop()

            for j in range(row, destination[0]):
                #path.append('V')
                dfs(path + ['V'], column, j + 1)
                #path.pop()
            return
        
        self.allRes = 0
        self.res = ''
        
        dfs([], 0, 0)
        return self.res