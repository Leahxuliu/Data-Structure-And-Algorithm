class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        res = []
        while n > 0:
            temp = (n - 1) * 26
            if temp >= k - 1:
                res.append(1)
                k -= 1
            else:
                res.append(k - temp)
                k = k - (k - temp)
        
            n -= 1
        
        print(res)
        string = ''
        for i in res:
            string += chr(i + 96)
        
        return string


# 优化
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        res = []
        while n > 0:
            temp = (n - 1) * 26
            if temp > k - 1:
                res.append('a')
                k -= 1
            else:
                temp = k - temp
                if temp != 26:
                    res.append(chr(temp + 96))
                    k = k - temp
                else:
                    res.append('z' * n)
                    break
            n -= 1
        
        return ''.join(res)