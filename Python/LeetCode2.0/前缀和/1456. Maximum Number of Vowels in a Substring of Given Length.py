#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/24

'''
Method - brute force
Steps:
    1. traverse s[i: i + k], i is from 0 to len(s) - k
    2. count the number of vowels in s[i:i + k]


optimal - two pointer
Steps:
    1. count the number of vowels in s[:k + 1]
    2. i start at 0, j start at k
    3. if nums[i] is vowels and nums[j] is vowels, i += 1, j +=1
        if nums[i] is not vowels and nums[j] is vowels, i += 1, j += 1, temp_res += 1,renew all_res
        if nums[i] is vowels and nums[j] is not, i+= 1, j+= 1,temp_res - 1
        

prefix - sum
accumulate the vowels numb in i in s

'''

# brute force
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        for i in range(0, len(s) - k + 1):
            temp = 0
            for j in s[i:i + k]:
                if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                    temp += 1
            res = max(temp, res)
        return res

# two pointer
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        
        for j in s[0:k]:
            if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
                res += 1
        
        i, j = 0, k
        temp = res
        
        while j < len(s):
            if s[i] not in 'aeiou' and s[j] in 'aeiou':
                temp += 1
                res = max(res, temp)
            elif s[i] in 'aeiou' and s[j] not in 'aeiou':
                temp -= 1
            i += 1
            j += 1
        return res

# prefix
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        prefix = [0] * n
        if s[0] in ['a', 'e', 'i', 'o', 'u']:
            prefix[0] = 1
        else:
            prefix[0] = 0
            
        for i in range(1, n):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                prefix[i] += prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]
        
        res = prefix[k - 1]
        for i in range(k, n):
            res = max(res, prefix[i] - prefix[i - k])
        return res