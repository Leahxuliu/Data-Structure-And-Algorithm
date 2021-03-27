# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/18

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subseq = defaultdict(int)
        l = 0
        res = 0
        repeatCount = 0
        
        for i, each_s in enumerate(s):
            if subseq[each_s] >= 1:
                repeatCount  += 1
            subseq[each_s] += 1

            while repeatCount > 0:
                subseq[s[l]] -= 1
                if subseq[s[l]] == 1:
                    repeatCount -= 1
                l += 1
            
            res = max(res, i - l + 1)
        
        return res


# 记录重复的字母
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subseq = defaultdict(int)
        l = 0
        res = 0
        repeat = ''
        
        for i, each_s in enumerate(s):
            if subseq[each_s] >= 1:
                repeat = each_s
            subseq[each_s] += 1

            while repeat != '':
                subseq[s[l]] -= 1
                if s[l] == repeat:
                    repeat = ''
                l += 1
            
            res = max(res, i - l + 1)
        
        return res


from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left = 0
        visited = defaultdict(int)
        res = 0

        for right in range(len(s)):
            curr = s[right]
            visited[curr] += 1

            while visited[curr] > 1:
                visited[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return max(res, right - left + 1)