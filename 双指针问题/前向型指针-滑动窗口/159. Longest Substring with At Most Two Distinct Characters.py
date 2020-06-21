# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/19

'''
input: a string(s), all samll letter? A == a ? the lengh of the string is from 0 to inf
output: a substring with 2 Characters 

Method 
key: using sliding window to clarify the range and using dictionary to store the characters and how many times has the character appeared
1. start two pointers, r and l, both start at 0
2. store the characters into dict and use a 'count' to count how many characters in s[l, r+1]
3. if count <= 2, move r, r += 1
    else, move l until count to be 2 again (restore dict)
    store the length when the count is 2 (each time stor the longest)
4. repeat step2 and step3 until r has been moved to end of s


'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if s == '':
            return 0
        
        l = 0
        c_info = defaultdict(int)
        count = 0
        res = 0
        
        for r, each_s in enumerate(s):
            if c_info[each_s] < 1:
                count += 1
            c_info[each_s] += 1
            while count > 2:
                c_info[s[l]] -= 1
                if c_info[s[l]] == 0:
                    count -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res