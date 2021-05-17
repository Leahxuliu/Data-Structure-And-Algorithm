'''
从右到左遍历i
i比i+1小，则减
i比i+1大或等于，则加

'''

class Solution:
    def romanToInt(self, s: str) -> int:
        if s == '':
            return 0
        
        info = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = info[s[-1]]
        pre = info[s[-1]]
        n = len(s)
        for i in range(n - 2, -1, -1):
            curr = info[s[i]]
            if curr >= pre:
                res += curr
            else:
                res -= curr
            pre = curr
        return res