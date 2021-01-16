'''
Union find
allowedSwaps --> adjacent list
the diff in soure and target --> pair --> check in graph or not
'''

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        gT = [i for i in range(len(source))]
        rank = [1] * len(source)
        
        def connect(i, j):
            root1 = root(i)
            root2 = root(j)
            if root1 == root2:
                return
            if rank[root1] > rank[root2]:
                gT[root2] = root1
                rank[root1] += rank[root2]
            else:
                gT[root1] = root2
                rank[root2] += rank[root1]
            return
                
        def root(i):
            while gT[i] != i:
                gT[i] = gT[gT[i]]
                i = gT[i]
            return i
        
        def find(i, j):
            return True if gT[i] == gT[j] else False
        
        for i, j in allowedSwaps:
            connect(i, j)
        
        for i in range(len(gT)):
            gT[i] = root(i)
        
        info = {}
        same = set()
        for i, each in enumerate(target):
            if each not in info:
                info[each] = [i]
            else:
                info[each].append(i)
        
        res = 0
        for i, each in enumerate(source):
            #if source[i] == target[i]:
            #    continue
            
            flag = False
            if each in info:
                for j, index in enumerate(info[each]):
                    if find(i, index):
                        info[each].pop(j)
                        flag = True
                        break

            if flag == False:
                res += 1
        return res
        
# 优化
# 找不在一个组的

'''
Union find
allowedSwaps --> adjacent list
the diff in soure and target --> pair --> check in graph or not
'''

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        gT = [i for i in range(len(source))]
        rank = [1] * len(source)
        
        def connect(i, j):
            root1 = root(i)
            root2 = root(j)
            if root1 == root2:
                return
            if rank[root1] > rank[root2]:
                gT[root2] = root1
                rank[root1] += rank[root2]
            else:
                gT[root1] = root2
                rank[root2] += rank[root1]
            return
                
        def root(i):
            while gT[i] != i:
                gT[i] = gT[gT[i]]
                i = gT[i]
            return i
        
        def find(i, j):
            return True if gT[i] == gT[j] else False
        
        for i, j in allowedSwaps:
            connect(i, j)
        
        info = collections.defaultdict(list)
        for i in range(len(gT)):
            r = root(i)
            gT[i] = r
            info[r].append(i)
        
        res = 0
        for k, v in info.items():
            a = [source[i] for i in v]
            b = Counter([target[i] for i in v])
            for each in a:
                if b[each] == 0:
                    res += 1
                else:
                    b[each] -= 1
        return res