#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/23

'''
Method - Two pointers
Steps:
    1. set i, j, z, at m - 1, n - 1, m + n - 1
    2. if nums1[i] >= nums2[j], nums1[z] = nums1[i], i - 1, z - 1
       else, nums1[z] = nums2[j], j - 1, z - 1
    3. repeat step2 until i < 0 or j < 0
    4. if j >= 0, nums1[:z + 1] = nums[:j + 1] 

Time: O(m + n)
Space: O(1)

'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, z = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[z] = nums1[i]
                i -= 1
                z -= 1
            else:
                nums1[z] = nums2[j]
                j -= 1
                z -= 1
        
        if j >= 0:
            nums1[:z + 1] = nums2[:j + 1]