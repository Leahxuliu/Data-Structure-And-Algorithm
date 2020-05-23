#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/23

'''
Method - two pointers
Steps:
    

Time: O(MN)
Space:O(1)

'''

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        '''res = 0
        for W in words:
            if self.check(S, W) == True:
                res += 1
        return res'''

        return sum(self.check(S, W) for W in words)

    def check(self, S, W):
        i, j, n, m = 0, 0, len(S), len(W)
        for i in range(n):
            if j < m and S[i] == W[j]:
                j += 1
            elif S[i - 1:i + 2] != S[i] * 3 != S[i - 2:i + 1]:
                return False
        return j == m
