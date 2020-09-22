'''class MySolution:
    def findPath(self, grid):

        visit = [[False] * len(grid) for _ in range(len(grid[0]))]
        def dfs(i, j, visited, all_path, path):  # i: 行; j: 列
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                all_path.append(path[:])

            visited[i][j] = True
            path.append(grid[i][j])
            if i - 1 >=0 and not visit[i][j]:
                dfs(i - 1, j, visited, all_path, path)  # 上走一格
            if i + 1 <= len(grid) - 1 and not visit[i][j]:
                dfs(i + 1, j, visited, all_path, path)  # 下走一格
            if j  - 1 >= 0 and not visit[i][j]:
                dfs(i, j - 1, visited, all_path, path)  # 左走一格
            if j + 1 <= len(grid[0]) - 1 and not visit[i][j]:
                dfs(i, j + 1, visited, all_path, path)  # 右走一格
            path.pop()
            visited[i][j] = False

        all_path = []
        dfs(0,0,visit,all_path,[])
        return all_path'''

'''
x = MySolution()
print(x.findPath([[0,1,2],[3,4,5]]))'''


class permutation:
    def permute(self, nums):
        res = []
        temp = []

        def backtrack(res, temp):
            if len(temp) == len(res):
                res.append(temp[:])
            else:
                for i in nums:
                    if i not in temp:
                        temp.append(i)
                        backtrack(res, temp)
                        temp.pop()
        backtrack(res,temp)
        return res

x = permutation()
print(x.permute([1,2,3]))

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, nums):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in nums:
                if i in path:
                    continue
                path.append(i)
                backtrack(path, nums)
                path.pop()

        backtrack([], nums)
        return res