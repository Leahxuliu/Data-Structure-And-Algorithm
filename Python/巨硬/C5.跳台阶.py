'''
跳台阶，两个参数（n级台阶，最多可迈k步）
'''

'''
70
k=2
'''

def count(n, k):
    if n == 0:
        return 0
    
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        if i <= k:
            for j in range(i):
                dp[i] += dp[j]
            dp[i] += 1
        else:
            for j in range(1, k + 1):
                dp[i] += dp[i - j]
    return dp[-1]




    
