# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04  
# @Author  : XU Liu
# @FileName: 

'''
1. 题目类型：
    DP
    背包问题

2. 题目要求与理解：
    给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
    其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
    例子：
    N = 3, W = 4
    wt = [2, 1, 3]
    val = [4, 2, 3]

3. 解题思路：
    二维dp， dp：N+1 * W+1
    dp[i][w]表示价值
    状态转移方程：
        dp[i][w] = max(选i，不选i)
            不选：dp[i][w] = dp[i-1][w]
            选：dp[i][w] = dp[i-1][w-wt[i-1]] + val[i-1]
        dp[0][..] = 0
        dp[..][0] = 0
    归纳：
        if i == 0 or w == 0:
            dp[i][w] = 0
        elif wt[i-1] > w:
            dp[i][w] = dp[i-1][w]
        elif wt[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + val[i-1])


    return dp[N][W]

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

'''
递归
'''


'''
递归 + memo
'''

'''
dp
'''
def bag(N, W, wt, val):
    if N == 0 or W == 0:
        return 0
    
    m = len(wt)
    dp = [[0] * (W + 1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for w in range(1, W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
            elif wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + val[i-1])
    return dp[N][W], dp


def show(N, W, wt, dp):
    x = [False for i in range(N)]
    j = W
    for i in range(1,N+1):  
        if dp[i][j] > dp[i-1][j]:  
            x[i-1] = True  
            j -= wt[i-1]  
    print('选择的物品为:')  
    for i in range(N):  
        if x[i]:  
            print('第' + str(i) + '个: ' + '重量为' + str(wt[i]) + '价值为' + str(val[i])) 


if __name__ == '__main__':
    N = 5
    W = 20
    wt = [2, 3, 4, 5, 9]
    val = [3, 4, 5, 8, 10]
    res, dp = bag(N, W, wt, val)
    print(res)
    show(N, W, wt, dp)