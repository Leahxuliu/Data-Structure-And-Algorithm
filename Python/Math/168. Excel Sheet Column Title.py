'''
26
26 + 26 * 26
26 + 26 * 26 + 26 * 26 * 26
'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 0:
            character = n % 26
            n = n // 26
            if character == 0:
                res = 'Z' + res
                n -= 1
            else:
                res = chr(character + 64) + res

        return res