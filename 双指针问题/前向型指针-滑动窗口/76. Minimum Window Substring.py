# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/18

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == '':
            return ''
        
        info = {}
        for i in t:
            if i in info:
                info[i] += 1
            else:
                info[i] = 1
        
        l = 0
        count = len(t)
        res = (0, len(s))
    
        for r in range(len(s)):
            if s[r] in info:
                if info[s[r]] > 0:
                    count -= 1
                info[s[r]] -= 1
                    
                while count == 0:
                    if r - l < res[1] - res[0]:
                        res = (l, r)
                        
                    if s[l] in info:
                        if info[s[l]] == 0:
                            count += 1
                        info[s[l]] += 1
                    l += 1
        if res == (0, len(s)):
            return ''
        else:
            return s[res[0]:res[1] + 1]


from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == '' or t =='':
            return ''
        
        substr = defaultdict(int)
        for i in t:
            substr[i] += 1
            
        l = 0
        count = len(t)
        res = (0, len(s))
        
        for r, each_s in enumerate(s):
            if substr[each_s] > 0:
                count -= 1
            substr[each_s] -= 1
            while count == 0 and l <= r:
                if r - l < res[1] - res[0]:  # 为什么写在这，与题目3的区别是什么？ 因为题目三，while里面是不符合题目的答案，需要while之后的答案才符合；而这题是相反的；考虑哪个位置符合题目条件
                    res = (l, r)
               
                if substr[s[l]] == 0:
                    count += 1
                substr[s[l]] += 1
                l += 1
                
            
        if res == (0, len(s)):
            return ''
        else:
            return s[res[0]:res[1] + 1]
            
        
        
    
            
            