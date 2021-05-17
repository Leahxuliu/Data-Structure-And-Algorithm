'''
单向BFS
'''
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                graph[key].append(word)
        
        queue = deque()
        queue.append([beginWord, []])
        visited = set()
        visited.add(beginWord)

        while queue:
            node, path = queue.popleft()
            path.append(node)

            if node == endWord:
                return len(path)
            
            for i in range(len(node)):
                key =  node[:i] + '*' + node[i + 1:]
                for out in graph[key]:
                    if out not in visited:
                        queue.append([out, path[:]])
                        visited.add(out)
        return 0


'''
双向BFS

1. 建立两个queue和两个visited
2. 判断是否已经遍历过，同对方的visited
3. 每次迭代size小的那个queue

'''
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                graph[key].append(word)

            
        
        s_queue, e_queue = deque(), deque()
        s_queue.append(beginWord)
        e_queue.append(endWord)

        s_visited, e_visited = set(), set()
        s_visited.add(beginWord)
        e_visited.add(endWord)

        step = 0

        
        while s_queue:
            if len(s_queue) > len(e_queue):
                e_queue, s_queue = s_queue, e_queue
                e_visited, s_visited = s_visited, e_visited

            step += 1
            q_len = len(s_queue)
            for _ in range(q_len):
                node = s_queue.popleft()
                if node in e_visited:
                    return step

                for i in range(len(node)):
                    key =  node[:i] + '*' + node[i + 1:]
                    for out in graph[key]:
                        if out not in s_visited:
                            s_queue.append(out)
                            s_visited.add(out)

        return 0

