'''
204. Count Primes

'''

class Solution:
    def countPrimes(self, n: int) -> int:
        """count the primes numbers which is less than  n

        Args:
            n: int
        
        Returns:
            n: int, the number of primes
        """
        # corner case
        if n == 0 or n == 1:
            return 0

        ans = [1] * n
        ans[0] = 0
        ans[1] = 0

        max_value = int(n ** 0.5)
        for i in range(2, max_value + 1):
            if ans[i] == 1:
                times = 2
                while i * times < n:
                    ans[i * times] = 0
                    times += 1
        return sum(ans)


# 给定正整数n，求小于n的质数的和 
ans = [each for each in range(n)]