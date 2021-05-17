'''
有向图的拓扑排序
有环 return ""
'''
from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if words == []:
            return ""
        
        visited = {}
        for each in words:
            for i in each:
                visited[i] = -1

        # 核心
        graph = defaultdict(set)
        for i in range(len(words) - 1):
            # 找到第一个不一样的
            flag = False
            for w1, w2 in zip(words[i], words[i + 1]):
                if w1 != w2:
                    graph[w1].add(w2)
                    flag = True
                    break
            # 例如["abc","ab"] 不符合
            if flag == False and len(words[i]) > len(words[i + 1]):
                return ''

        def find(char):
            '''return True if no circle
            '''

            if visited[char] == 0:
                return False
            if visited[char] == 1:
                return True

            visited[char] = 0
            for out in graph[char]:
                if find(out) == False:
                    return False
            visited[char] = 1
            res.append(char)
            return True
        
        res = []
        for k, v in visited.items():
            if v == -1:
                if find(k) == False:
                    print(k)
                    return ''
        return ''.join(res[::-1])

