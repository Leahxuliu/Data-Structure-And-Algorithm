class Solution:
    def findCircleNum(self, M) -> int:
        if len(M) == 1:  # corner case
            return 1

        m = len(M)
        graphTag = [i for i in range(m)]

        times = 0
        for i in range(m):
            for j in range(i + 1):
                if M[i][j] == 1:
                    root1 = self.find(i, graphTag)
                    root2 = self.find(j, graphTag)
                    if root1 == root2:
                        pass
                    else:
                        graphTag[root2] = root1
                        times += 1
        return m - times

    def find(self, i, graph):  # return root index of i node
        if graph[i] == i:
            return i
        else:
            return self.find(graph[i], graph)

x = Solution()
print(x.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))