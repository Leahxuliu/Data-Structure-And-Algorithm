from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        left = 0
        right = 0
        info = defaultdict(int)
        res = 0

        for right in range(len(s)):
            info[s[right]] += 1

            while info[s[right]] > 1:
                info[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res    
