'''
相似题 168

数字转字母需要考虑1-based什么的
字母转数字不需要考虑，直接res = res * 26 + now就可
'''


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if columnTitle == '':
            return 0
        
        res = 0
        
        for char in columnTitle:
            res = res * 26 + ord(char) - 64
        
        return res