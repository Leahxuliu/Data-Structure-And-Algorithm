'''
模拟成26位进制，不同的地方在于1-based
余数0的时候 -> Z, div也要-1
最后不要忘记res要转置

数字转字母需要考虑1-based什么的
字母转数字不需要考虑，直接res = res * 26 + now就可

相似题171

'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ''
        
        res = ''

        while columnNumber:
            div, rem = divmod(columnNumber, 26)
            if rem == 0:
                res += 'Z'
                div -= 1
            else:
                res += chr(64 + rem)
            columnNumber = div
        return res[::-1]