'''
b / a = 3c / 6c = 0.5 把‘不同的变量’转换成‘相同变量’的倍数

一边查询一边修改

路径压缩
 
  2.0   3.0
a --> b --> c

  6.0   3.0
a --> c <-- b
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gT = {}
        weight = {}

        def add(i):
            if i not in gT:
                gT[i] = i
                weight[i] = 1.0
            return
        
        def find(i):
            if i != gT[i]:
                origin = gT[i]
                gT[i] = find(gT[i])
                # 更新点
                weight[i] *= weight[origin]
            return gT[i]
        
        def union(i, j, val):
            root1 = find(i)
            root2 = find(j)

            if root1 != root2:
                gT[root1] = root2
                # 更新点
                # 四边形法则更新根节点的权重
                weight[root1] = weight[j] * val / weight[i]
            return


        for (a, b), val in zip(equations, values):
            add(a)
            add(b)
            union(a, b, val)

        res = []
        for (a, b) in queries:
            if a in weight and b in weight and find(a) == find(b):
                res.append(weight[a] / weight[b])
            else:
                res.append(-1.0)
        return res
