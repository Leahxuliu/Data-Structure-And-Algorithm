'''
LC 3
'''
'''
slide window
'''
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
        res = max(res, right - left + 1)
        return res

        


'''
若允许重复一次
'''

def lengthOfLongestSubstring(s):
    if len(s) < 2:
        return len(s)
    
    left = 0
    visited = defaultdict(int)
    res = 0

    for right in range(len(s)):
        curr = s[right]
        visited[curr] += 1

        while visited[curr] > 2:
            visited[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)
    res = max(res, right - left + 1)
    return res

print(lengthOfLongestSubstring("tmmzuxt"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
