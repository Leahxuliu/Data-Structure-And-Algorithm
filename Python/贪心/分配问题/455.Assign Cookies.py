# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/05  
# @Author  : XU Liu
# @FileName: 455.Assign Cookies.py

'''
1. 题目要求：


2. 理解：


3. 输出输入以及边界条件：
input: 
output: 
corner case: 

4. 解题思路
    
5. 空间时间复杂度

'''

# 贪心 + two point
# 时间复杂度 O(min(m, n))
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g == [] or s == []:
            return 
        
        g.sort()
        s.sort()
        
        i, j = 0, 0
        res = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # 关键点，不仅仅是等于的时候 
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res


# 像greedy模版的写法
# 时间复杂度高
# 时间复杂度 O(max(m, n))
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s == [] or g == []:
            return 0
        
        g.sort()
        s.sort()
        res = 0
        j = 0
        for i in g:
            while j < len(s):
                if i <= s[j]:
                    res += 1
                    j += 1
                    break
                j += 1
                
        return res