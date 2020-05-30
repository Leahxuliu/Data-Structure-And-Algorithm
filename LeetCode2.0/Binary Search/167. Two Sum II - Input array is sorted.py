#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/30


# dict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers == []:
            return []

        info = {}
        for i, n in enumerate(numbers):
            temp = target - n
            if temp in info:
                return [info[temp] + 1, i + 1]
            info[n] = i
        return []

# Two pointer
'''
对撞双指针
[1,2,3,4,5]
头 + 尾 是两两数相加里面的平均值
参考高斯求和

i, j = 0, len(arr) - 1
arr[i] + arr[j] == target --> return
arr[i] + arr[j] > target  --> j -= 1
arr[i] + arr[j] < target  --> i += 1
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers == []:
            return []

        i, j = 0, len(numbers) - 1

        while i < j:
            temp = numbers[i] + numbers[j]
            if temp == target:
                return [i + 1, j + 1]
            if temp > target:
                j -= 1
            if temp < target:
                i += 1
        return []


# binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers == []:
            return []

        n = len(numbers)
        for i in range(n):
            l = i + 1  # 易错，要加1
            r = n - 1

            while l <= r:
                mid = l + (r - l) // 2
                temp = numbers[i] + numbers[mid]
                if temp == target:
                    return [i + 1, mid + 1]
                if temp > target:
                    r = mid - 1
                elif temp < target:
                    l = mid + 1
        return []
