'''
奇数个的char最多只能有一个
'''
from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if s == '':
            return True

        info = defaultdict(int)
        for i in s:
            info[i] += 1
        
        count = 0
        for v in info.values():
            if v % 2 == 1:
                count += 1
                if count >= 2:
                    return False
        return True