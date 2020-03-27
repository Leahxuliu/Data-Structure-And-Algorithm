#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/27  
# @Author  : XU Liu
# @FileName: 367.Valid Perfect Square.py

'''
1. 题目理解：
    判断给到的数字是不是可以被开平方
    不能使用 sqrt function
    16 --> 4 * 4 --> true
    14 -->  None --> False

2. 题目类型：
    binary sort
    target

3. 输出输入以及边界条件：
input:  int
output: bool
corner case: 0,1,2 

4. 解题思路
    binary search
    ##Memory Limit Exceeded##
    1. make a list, such as[1,2,3,4....,16] 易错 arr = [i+1 for i in range(num)] 从1开始到num
    2. arr[mid] * arr[mid] == target 
    
    改进：
    不要写arr，arr造成Memory Limit Exceeded
    另外先num//2之后再binary search
    注意0，1，2

    from 李厨子
    Newton
    牛顿法（又称：牛顿迭代法）
    见笔记本
    time O(logN)
    space O(1)
    
5. 时间空间复杂度：
    time: O(logN)
    space: 1

'''

'''
超容量
'''
class Solution:
    def isPerfectSquare(self, num):
        if num == 0 or num == 1 or num == 2:
            return True
        
        arr = [i+1 for i in range(num//2)]
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if arr[mid] * arr[mid] == num:
                return True
            elif arr[mid] * arr[mid] > num:
                r = mid - 1
            elif arr[mid] * arr[mid] < num:
                l = mid + 1
        return False

'''
改进
不要arr，在l，r上面下功夫
'''
class Solution:
    def isPerfectSquare(self, num):
        if num == 0 or num == 1 or num == 2:
            return True
        
        l, r = 0, num // 2  # 难点
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
        return False


'''
改进 Newton
'''
class Solution2:
    def isPerfectSquare2(self, num):
        if num == 1:
            return True
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num


x = Solution()
print(x.isPerfectSquare(4))