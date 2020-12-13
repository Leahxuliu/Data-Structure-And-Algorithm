# 超时
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 0

        res = []

        for i in range(2, n):  # n: 0 to n-1
            flag = False
            for j in res:
                if i % j == 0:
                    flag = True
                    break
            if flag == False:
                res.append(i)
        return len(res)
        
'''
建立一个lst，每一个index就代表该integer，初始是1，1表示是素数
lst[0] = 0, lst[1] = 0, 0和1都是素数
从2开始遍历
2的倍数的integer都不是素数，lst[2 * times] = 0
反复循环
当遍历到的数，i*i > n的时候就可以停止遍历了
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 0

        lst = [1] * n  # 1 represent prime
        lst[0] = 0
        lst[1] = 0

        for i in range(2, n):  # n: 0 to n-1
            if i * i > n:
                break
            
            if lst[i] == 1:
                times = 2
                while times * i < n:
                    lst[times * i] = 0
                    times += 1

        return sum(lst)