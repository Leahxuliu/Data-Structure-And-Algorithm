'''
遍历罗马字符串
if i >= i + 1 则res += i
if i < i + 1 则res -= i
最后一个直接加
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        info = {'I': 1, 'V':5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                res += info[s[i]]
            else:
                if info[s[i]] >= info[s[i + 1]]:
                    res += info[s[i]]
                else:
                    res -= info[s[i]]
        return res