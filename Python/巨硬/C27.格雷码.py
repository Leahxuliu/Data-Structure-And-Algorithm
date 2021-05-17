'''
89
gray code
'''

'''
1. 在前一个状态的基础上，前面加0或者1
2. 加0的时候，保持前一个状态时的顺序
   加1的时候，保持前一个状态的倒序，在前面加1也就是意味着加2**n
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        head = 1
        res = [0]

        for _ in range(n):
            len_res = len(res)
            for i in range(len_res - 1, -1, -1):
                res.append(res[i] + head)
            head = head << 1
        return res
