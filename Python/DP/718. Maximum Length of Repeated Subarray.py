'''
超时
1. 把其中一个数组保存到dict里面，key是number， value是index
2. 用双指针遍历并比对

'''
from collections import defaultdict
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if A == [] or B == []:
            return 0
        
        info = defaultdict(list)
        for i in range(len(A)):
            info[A[i]].append(i)
        
        res = 0
        for i in range(len(B)):
            for j in info[B[i]]:
                x = i 
                y = j 
                while x < len(B) and y < len(A):
                    if B[x] != A[y]:
                        break
                    else:
                        x += 1
                        y += 1
                res = max(res, x - i)
        return res


'''
dp

dp[i][j] 表示 A[i:] 和 B[j:] 的最长公共前缀
答案即为所有 dp[i][j] 中的最大值

也就是A[i:]要全在B[j:]里面
'''


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if A == [] or B == []:
            return 0
        
        m = len(A)
        n = len(B)

        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res
