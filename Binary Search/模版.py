#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03/24  
# @Author  : XU Liu
# @FileName: 模版.py


# 模板1
# 有一个Edge的情况就是，L最大可以等于len(array)，R最小可能为-1
def binarySearch(arr, target):    
    l, r = 0, len(arr) - 1
    while l <= r: # l和r互换位置相邻时，返回
        mid = l + (r - l) //2  # 是L，不是1；mid对于偶数，是靠左的，即[1,2]中，mid为1
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1
    return -1

# 极个别情况下的模板
# 针对的是第一个模板的短板：当要access数组边界的数，如果边界的数在运行中出现更改，可能越界。??
# 虽然这种情况也可以用Edge Case来写，但太过麻烦。这点我们后面具体说来。
def binarySearch(arr, target):
    l, r = 0, len(arr) - 1
    while l + 1 < r:  # r要比l大2，即中间可以隔一个数，[0,2]不返回；l和r相邻时，返回
        mid = l + (r - l) //2
        if target == arr[mid]:  # 不仅mid为结果值
            l = mid
        elif target < arr[mid]:
            r = mid
        elif target > arr[mid]:
            l = mid
    
    if arr[l] == target:
        return l
    if arr[r] == target:
        return r
    return -1

