
# 方法一 超时
# 遍历所有情况
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        column = len(heights[0])
        
        visited = [[0] * column for _ in range(row)]
        
        def helper(i, j, visited, cost):
            if i == row - 1 and j == column - 1:
                res.append(cost)
            if visited[i][j] == 1:
                return 
            
            visited[i][j] = 1
            if i - 1 >= 0:
                helper(i - 1, j, visited, max(cost, abs(heights[i][j] - heights[i - 1][j])))
            if j - 1 >= 0:
                helper(i, j - 1, visited, max(cost, abs(heights[i][j] - heights[i][j - 1])))
            if i + 1 <= row - 1:
                helper(i + 1, j, visited, max(cost, abs(heights[i][j] - heights[i + 1][j])))
            if j + 1 <= column - 1:
                helper(i, j + 1, visited, max(cost, abs(heights[i][j] - heights[i][j + 1])))
            # 重点
            visited[i][j] = 0

                    
        res = []
        
        helper(0, 0, visited, 0)
        print(res)
        return min(res)



import java.util.ArrayList;

class Solution {
    private int row;
    private int column;
    private int vis[][] = new int[101][101];
    ArrayList<Integer> res =new ArrayList<>();

    public int minimumEffortPath(int[][] heights) {
        helper(0, 0, 0, heights);
        return Collections.min(res);
    }

    private void helper(int i, int j, int cost, int[][] heights) {
        if (i == heights.length - 1 && j == heights[0].length - 1) {
            res.add(cost);
        }

        if (vis[i][j] == 1) {
            return;
        }

        vis[i][j] = 1;

        if (i - 1 >= 0) {
            helper(i - 1, j, Math.max(cost, Math.abs(heights[i][j] - heights[i - 1][j])), heights);
        }
        if (j - 1 >= 0) {
            helper(i, j - 1, Math.max(cost, Math.abs(heights[i][j] - heights[i][j - 1])), heights);
        }
        if (i + 1 < heights.length) {
            helper(i + 1, j, Math.max(cost, Math.abs(heights[i][j] - heights[i + 1][j])), heights);
        }
        if (j + 1 < heights[0].length) {
            helper(i, j + 1, Math.max(cost, Math.abs(heights[i][j] - heights[i][j + 1])), heights);
        }
        vis[i][j] = 0;
    }
}