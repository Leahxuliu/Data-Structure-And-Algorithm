# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/10

'''
{}内是可选

step
1. Extract letters in {}, put the words into the list
    [[a,b], [c], [d,e], [f]]
2. use backtracking? dfs? to find all options

'''

# dfs
'''
time   O(n * m * q * ...) n/m/q... len(words[i])
space  O(N)
'''
class Solution:
    def expand(self, S: str) -> List[str]:
        if S == '':
            return []
        
        # 处理S
        # "{a,b}c{d,e}fg" --> [['a', 'b'], ['c'], ['d', 'e'], ['f'], ['g']]
        flag = 0
        words = []
        for i in S:
            if i == '{':
                flag = 1
                words.append([])
            elif i == '}':
                flag = 0
            else:
                if flag == 1:
                    if i != ',':
                        words[-1].append(i)
                else:
                    words.append([i])
        # sort
        for i in range(len(words)):
            words[i].sort()

        # dfs
        # 画组合树，好理解，也就是求无头多叉树的path
        def dfs(index, s):
            for j in range(len(words[index])):
                if index == len(words) - 1:  # 写在for里面，没有return
                    #res.append(s + words[index][j])
                    res.append(''.join(s) + words[index][j])
                else:
                    #dfs(index + 1, s + words[index][j])
                    dfs(index + 1, s + [words[index][j]])

        res = []
        dfs(0, [])
        return res


# bfs
class Solution:
    def expand(self, S: str) -> List[str]:
        if S == '':
            return []
        
        # organize S
        words = []
        temp = []
        for i in S:
            if i == '{':
                if temp != []:
                    words.append([''.join(temp)])  # 易错
                temp = []
                
            elif i == '}':
                words.append(temp)
                temp = []
            else:
                if i != ',':
                    temp.append(i)
        if temp != []:
            words.append([''.join(temp)])  # 易错

        # sort
        for i in range(len(words)):
            words[i].sort()

        # use dfs to find all options
        def dfs(index, s):
            if index == len(words):  # 比上面那一种要慢
                res.append(s)
                return 

            for j in range(len(words[index])):
                
                dfs(index + 1, s + words[index][j])

        res = []
        dfs(0, '')
        return res


# backtracking

class Solution:
    def expand(self, S: str) -> List[str]:
        if S == '':
            return []
        
        # 处理S
        flag = 0
        words = []
        for i in S:
            if i == '{':
                flag = 1
                words.append([])
            elif i == '}':
                flag = 0
            else:
                if flag == 1:
                    if i != ',':
                        words[-1].append(i)
                else:
                    words.append([i])
        # sort
        for i in range(len(words)):
            words[i].sort()

        # backtracking
        def backtracking(index, s):
            if index == len(words):
                res.append(''.join(s))
                return
            for i in range(len(words[index])):
                s.append(words[index][i])
                backtracking(index + 1, s)
                s.pop()
        res = []
        backtracking(0, [])
        return(res)