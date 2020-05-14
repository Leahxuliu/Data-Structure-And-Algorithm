'''
Method - DFS
Steps:
    1. use edges to build graph
    2. use DFS to scan the vertexs(i) and the neighbors from graph
       if has apple, return True  
    3. calculate the number of edges when the apple is in the bottom apple's level
       eg: 2 is the bottom apple's level
       
Time complexity: O(N) N is the number of vertexs; traverse all vertexs
Space complexity:O(logN) the stack was used by recursion
    

'''

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if n == 0:
            return 0
        
        graph = [[] for _ in range(n)]
        
        for x, y in edges:
            graph[x].append(y)
            

        def DFS(i):  # traverse the tree, if has apple, return True    
            pre = False
            for out in graph[i]:
                if DFS(out) == True:
                    pre = True
                    self.res += 2
            return hasApple[i] or pre  # 判断这个点是不是有苹果以及这个点一下的点上面是不是有苹果
        
        self.res = 0
        DFS(0)
        return self.res
        