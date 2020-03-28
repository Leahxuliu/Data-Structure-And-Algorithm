#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/28  
# @Author  : XU Liu
# @FileName: 658.Find K Closest Elements.py

'''
1. 题目类型：
    binary search

2. 题目理解以及解题思路：
    难 不好理解啊啊啊啊
    在排序arr中，求某数x的周围k个数，若有左右相同的位置的数，取左边的数
    比如[1,2,3,4,5], k=3, x=3 --> expected [2,3,4]
    注意，arr中数字是可以重复的
    思路：
    1. 寻找i，使[i, i+k]符合题意，所以r改变成len(arr) - k - 1，而不是len(arr) - 1
    2. 把x看成mid和mid + k的中点
    3. 比较arr[mid], x, arr[mid+k]这三个值
    4. 要使得x-arr[mid]< arr[mid+k] - x
    5. 把arr[mid:mid+k]看作一整块，左右移动
       也就是说，比较框框内的第一个数字与x相差大还是框框外右边的第一个数字与x相差大
    5. x-arr[mid] = arr[mid+k] - x时，继续缩小右边界
    6. 最后返回找到的l，得到arr[l:l+k]

    最后返回找到的l值，得到arr[l:l+k]
    


3. 输出输入以及边界条件：
input: arr: List[int], k: int, x: int
output: list[int]
corner case: 


4. 时间空间复杂度：
    

'''


'''
题目理解错误
1. arr里面有重复
2. 找x最近的k个数，不能全部选择x前面的k个数

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == 1 and len(arr) == 1:
            return arr
        
        index = 0
        index = self.findTarget(arr, x)
        print(index)
        if k == 1:
            return [arr[index]]
        else:
            if index + 1 >= k:
                return arr[index - k:index]
            else:
                return arr[:k]
        
    
    def findTarget(self, arr, x):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                r = mid - 1
            elif arr[mid] < x:
                l = mid + 1
        return r
'''


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1 - k
        while l <= r:
            mid = l + (r - l) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                r = mid - 1
            elif x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
        return arr[l:l+k]