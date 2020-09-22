# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/15  
# @Author  : XU Liu
# @FileName: 375.Guess Number Higher or Lower II.py

'''
1. 题目类型：


2. 题目要求与理解：
    猜数字，猜错付猜的数字额度的钱
    求至少需要拥有多少现金才能确保赢钱

    由于要求最坏情况，所以左右两个区间，应取最大花费。最坏情况下，要尽可能少花费，所以最终要取所有最坏情况下的最小花费值。

3. 解题思路：
    方案一：二分搜索
    方案二：DP

4. 输出输入以及边界条件：
input: n >= 1
output: int
corner case: 

5. 空间时间复杂度
    

'''

'''
报错
'''
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        def BTcount(l, r):
            temp = 0
            res = float('inf')
            
            while l <= r:
                mid = l + (r - l)//2
                temp = max(BTcount(l, mid - 1), BTcount(mid + 1, r)) + mid
                res = min(temp, res)
            return res
        
        return BTcount(1, n)


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def getcost(i,j,cost):            
            if cost[i][j] != -1:              
                return cost[i][j]
            if i == j :                              
                cost[i][j] = 0
                return 0
            if i + 1 == j:               
                cost[i][j] = i
                return i
            money = float("inf")
            for mid in range(i+1, j):
                left = mid + getcost(i,mid-1,cost)
                right = mid + getcost(mid+1,j,cost)
                if max(left,right) < money:
                    money = max(left,right)           
            cost[i][j] =  money 
            return money       
        cost = [ [-1 for _ in range(n+1)]  for _ in range(n+1)]
        getcost(1,n,cost)
        return cost[1][n]


def getMoneyAmount(self, n):
    need = [[0] * (n+1) for _ in range(n+1)]
    for lo in range(n, 0, -1):
        for hi in range(lo+1, n+1):
            need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])
                               for x in range(lo, hi))
    return need[1][n]