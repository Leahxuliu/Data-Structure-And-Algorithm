# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16  
# @Author  : XU Liu
# @FileName: 167.Two Sum II - Input array is sorted.py



'''
方法1 暴力解法
时间复杂度 O(N**2)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n-1):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]


'''
方法2 2分搜索
时间复杂度 O(logN)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers == []:
            return 
        
        n = len(numbers)
        for i in range(n):
            l = i + 1
            r = n - 1
            
            while l <= r:  # 这里的等号必须要有
                mid = l + (r - l) // 2
                sums = numbers[i] + numbers[mid]
                if sums == target:
                    return [i + 1, mid + 1]
                elif sums > target:
                    r = mid - 1
                elif sums < target:
                    l = mid + 1

'''
用字典来保存值
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        num_dict = {}
        for i in range(n):
            temp = target - numbers[i]
            if temp in num_dict:
                return [num_dict[temp] + 1, i + 1]
            else:
                num_dict[numbers[i]] = i