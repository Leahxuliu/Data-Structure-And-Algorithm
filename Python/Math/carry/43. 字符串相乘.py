'''
乘法运算规则

1. 两数相乘所得数的最长长度不超过m + n
2. num1[i] * num[j]的乘积分布在res[i + j]和res[i + j + 1]处
3. 核心
    curr = int(num1[i]) * int(num2[j]) + res[i + j + 1]
    res[i + j + 1] = curr % 10
    res[i + j] = curr // 10 + res[i + j]  # 易错

'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        n = len(num1)
        m = len(num2)
        res = [0] * (m + n)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                curr = int(num1[i]) * int(num2[j]) + res[i + j + 1]
                res[i + j + 1] = curr % 10
                res[i + j] = curr // 10 + res[i + j]  # 易错
            
        start = 0
        for i in range(len(res)):
            if res[i] != 0:
                start = i
                break
        # print(res, start)
        return ''.join(str(each) for each in res[start:])