#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
方法1：非原地算法
1. 选定pivot为第一个数
2. 重新排列数组，形成 小于pivot数组 - pivot - 大于pivot的数组
3. 再对小于pivot数组和大于pivot数组进行1，2两步
'''

class Sort:
    def quickSort(self, nums):  # return sorted nums
        if not nums or len(nums) == 1:  # corner case
            return nums

        pivot = nums[0]
        l = []
        r = []
        for elem in nums[1:]:
            if elem < pivot:
                l.append(elem)
            else:
                r.append(elem)
        left = self.quickSort(l)
        right = self.quickSort(r)
        nums = left + [pivot] + right
        return nums

'''
方法2：原地算法
难
'''
class Solution:
    def quickSort(self, arr):
        if len(arr) == 0 or len(arr) == 1:  # corner case
            return arr

        i, l = 0, 0
        j, r = len(arr) - 1, len(arr) - 1
        pivot = arr[i]

        while i < j:
            while i < j and pivot < arr[j]:  # 扫描一段去寻找合适的值, 循环条件是正常的顺序（pivot < arr[j]），若发现异常，则跳出更换i和j
                j -= 1
            arr[i] = arr[j]  # 搜寻一段之后，找到值，再替换
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]
        arr[i] = pivot  # i in center, give it pivot
        L = arr[:i]
        R = arr[i + 1:]
        arr[:i] = self.quickSort(L)  # L part = arr[0:i] < pivot
        arr[i + 1:] = self.quickSort(R)  # R part = arr[i + 1, j] > pivot
        return arr

