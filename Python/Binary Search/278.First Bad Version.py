#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/28  
# @Author  : XU Liu
# @FileName: 278.First Bad Version.py

'''
1. 题目理解：
    找到第一个不好的version
    后台有一个程序
    输入的值-->False 产品是好的
           -->True  产品是坏的
    找到第一个True的值

2. 题目类型：
    binary search

3. 输出输入以及边界条件：
input: int
output: int
corner case:  

4. 解题思路
    brute force
    n 是True --> n-1，找到第一个不是True的值
    n 是False --> n+1，找到第一个不是False的值

    binary search
    先不判断n是T还是F
    先判断n//2是T还是F
    每次都一半一半来

5. 时间空间复杂度：
    

'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

'''
brute force
超时
'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        tag = isBadVersion(n)
        
        if tag == True:
            
            while n >= 1:
                n -= 1
                if isBadVersion(n) == False:
                    return n + 1
        else:
            while n > 1:
                n += 1
                if isBadVersion(n) == True:
                    return n

'''
binary search
[ffffttttttttttttt]
'''

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) //2
            if isBadVersion(mid) == True:
                r = mid - 1
            else:
                l = mid + 1
        return l