#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/20

'''
Method - Two Pointer
Steps:
    1. sort nums1 and nums2
    2. set i, j at nums1[0], nums2[0]
    3. if nums[i] == nums[j], add nums[i] into res, i += 1, j += 1
       if nums[i] > nums[j], j += 1
       if nums[i] < nums[j], i += 1
    4. return res

Times: O(nlogn)
Sapce: O(1)

'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        
        if n == 0 or m == 0:
            return []
        
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        res = set()
        while i < n and j < m:
            
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return res