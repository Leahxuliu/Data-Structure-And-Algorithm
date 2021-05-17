'''
brout force - backtracking 模拟条件
'''

class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0:
            return 0
        
        def find(path, flag_A):
            if len(path) == n:
                self.res += 1
                # print(path)
                temp.append(''.join(path))
                return
            
            for each in ['A', 'L', 'P']:
                if each == 'A':
                    if flag_A == 0:
                        find(path + [each], 1)
                elif each == 'L':
                    if path[-2:] != ['L', 'L']:
                        find(path + [each], flag_A)
                else:
                    find(path + [each], flag_A)

            return 
        
        self.res = 0
        temp = list()
        find([], 0)
        print(len(temp))
        return self.res % (10 ** 9 + 7)

'''
DP
先算只有P、L的数量，再去套A

二维数组，dp[i][0]代表i这个位置为P时的数量，dp[i][1]时为i为L的数量
dp[i][0] = 上一个是p的情况 + 上一个是L的情况 = dp[i - 1][0] + dp[i - 1][1]
dp[i][1] = 上一个是p的情况 + 上两个是p的情况（相当于前面的第二个是P，前面一个是L）= dp[i - 1][0] + dp[i - 2][0]
没有A的所有情况：
ans = dp[n - 1][0] + dp[n - 1][1]

假如A放在i位置上，i之前有x个位置，i以后有y个位置
所以ans+=(dp[x-1][0]+dp[x-1][1])*(dp[y-1][0]+dp[y-1][1]);

每一步都除以mod，取余数
不然就会超时
'''

class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        if n == 2:
            return 8

        mod = 10 ** 9 + 7
        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = 1
        dp[0][1] = 1
        dp[1][0] = 2
        dp[1][1] = 2

        for i in range(2, n):
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % mod
            dp[i][1] = (dp[i - 1][0] + dp[i - 2][0]) % mod
        
        # 无A
        ans = (dp[n - 1][0] + dp[n - 1][1]) % mod
        # 有一个A
        # A在第一个或最后一个
        ans += (2 * (dp[n - 2][0] + dp[n - 2][1])) % mod

        # A在第二个之后
        for i in range(1, n - 1):
            ans += ((dp[i - 1][0]+dp[i - 1][1]) * (dp[n - i - 2][0] + dp[n - i - 2][1])) % mod
        return ans % mod