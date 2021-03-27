'''
brout force
traversal number from 1 to n
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # corner case
        if n == 0:
            return 0

        # count n!
        count = 1
        for i in range(1, n + 1):
            count *= i 
        
        # count the number of 0
        res = 0
        # while count > 0:
        #     if count % 10 == 0:
        #         res += 1
        #         count = count // 10
        #     else:
        #         break
        count = str(count)
        for i in range(len(count) - 1, -1, -1):
            if count[i] == '0':
                res += 1
            else:
                break
        return res


'''
一对2和5就会有一个0
2的个数比5的个数多，所以数因子5的个数即可

5， 10， 15， 20 各有一个5，也就是每间隔5，就有一个因子5
25，50，100，125 各有两个5，每间隔25，就还有一个因子5
依次类推
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # corner case
        if n == 0:
            return 0

        res = 0
        div = 5
        while div <= n:
            res += n // div
            div *= 5
        return res