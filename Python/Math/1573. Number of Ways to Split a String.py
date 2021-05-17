'''
超时

'''

import math
class Solution:
    def numWays(self, s: str) -> int:
        if s == '':
            return 0
        
        count = 0
        for i in s:
            if i == '1':
                count += 1
        
        if count % 3 != 0:
            return 0 
        
        count = count // 3
        if count == 0:
            return math.comb(len(s) - 1, 2)

        def find(start, K):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return 1
            
            count = 0
            res = 0
            for i in range(start, len(s)):
                if s[i] == '1':
                    count += 1
                
                if count == K:
                    res += find(i + 1, K)

                elif count > K:
                    break

            memo[start] = res 
            return res
        
        memo = {} 
        
        return find(0, count)


'''
数学问题
'''

import math
class Solution:
    def numWays(self, s: str) -> int:
        if s == '':
            return 0
        
        div = 10 ** 9 + 7

        ones = []
        for i, each in enumerate(s):
            if each == '1':
                ones.append(i)
        
        count = len(ones)
        if count % 3 != 0:
            return 0 
        
        count = count // 3
        if count == 0:
            return math.comb(len(s) - 1, 2) % div

        m1 = ones[count] - ones[count - 1]
        m2 = ones[2 * count] - ones[2 * count - 1]
        return (m1) * (m2) % div
        