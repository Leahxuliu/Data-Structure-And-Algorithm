'''
7. Reverse Integer
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        res = 0
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
        
        while x:
            div, rem = divmod(x, 10)
            res = res * 10 + rem 
            x = div

        res = flag * res 
        return res if -1 * (2 ** 31) <= res <= (2 ** 31 - 1) else 0 