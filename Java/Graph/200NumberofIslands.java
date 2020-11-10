// DFS
class NumberofIslands{
    private int[][] visited;
    public int numIslands(char[][] grid) {
        visited = new int[grid.length][grid[0].length];
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1' && visited[i][j] != 1) {
                    dfs(grid, i, j);
                    count += 1;
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == '0' || visited[i][j] == 1) {
            return;
        }

        visited[i][j] = 1;

        dfs(grid, i + 1, j);
        dfs(grid, i - 1, j);
        dfs(grid, i, j + 1);
        dfs(grid, i, j - 1);
        return;

    }
}

// BFS
class Solution {
    public int numIslands(char[][] grid) {
        int[][] visited = new int[grid.length][grid[0].length];
        Queue<int[]> neighbors = new LinkedList<>();

        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1' && visited[i][j] != 1) {
                    neighbors.add(new int[] {i, j});
                    visited[i][j] = 1;
                    count += 1;

                    while (!neighbors.isEmpty()) {
                        int[] curr = neighbors.remove();
                        int x = curr[0];
                        int y = curr[1];

                        int[][] pattern = {{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}};
                        for (int[] newPos: pattern) {
                            int newX = newPos[0];
                            int newY = newPos[1];

                            if (newX >= 0 && newX < grid.length && newY >= 0 && newY < grid[0].length) {
                                if (grid[newX][newY] == '1' && visited[newX][newY] != 1) {
                                    neighbors.add(new int[] {newX, newY});
                                    visited[newX][newY] = 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
}

// 并查集
class Solution {
    private int[] gT;
    private int[] rank;
    private int count = 0;
    private int water = 0;

    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        gT = new int[n * m];
        rank = new int[n * m];

        for (int i = 0; i < n * m; i++) {
            gT[i] = i;
            rank[i] = 1;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '0') {
                    water += 1;
                } else {
                    if (i + 1 < n && grid[i + 1][j] == '1') {
                        UnionFind(i * m + j, (i + 1) * m + j, grid);
                    }
                    if (j + 1 < m && grid[i][j + 1] == '1') {
                        UnionFind(i * m + j, i * m + j + 1, grid);
                    }
                }
            }
        }
        return n * m - water - count;
    }

    private void UnionFind(int x, int y, char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        int root1 = find(x);
        int root2 = find(y);

        if (root1 == root2) {
            return;
        }

        count += 1;
        if (rank[root1] >= rank[root2]) {
            gT[root2] = root1;
            rank[root1] += rank[root2];
        } else {
            gT[root1] = root2;
            rank[root2] += rank[root1];
        }
    }

    private int find(int x) {
        while (gT[x] != x) {
            gT[x] = gT[gT[x]];
            x = gT[x];
        }
        return x;
    }
}
