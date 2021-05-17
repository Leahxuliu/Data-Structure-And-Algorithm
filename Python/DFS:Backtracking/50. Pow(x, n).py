'''
分治法 log(n)
注意n的正负
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        def count(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            mid = n // 2
            half = self.myPow(x, mid)

            return half * half if mid * 2 == n else half * half * x
        
        # 易忘
        if n < 0:
            x = 1 / x
            n = -n
        return count(x, n)