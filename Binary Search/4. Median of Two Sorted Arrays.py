#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/16

'''
Method - Two pointer
1. len(nums1) + len(nums2), find the median [med]
2. set two pointers i, j at 0(nums1), 0(nums2)
3. if nums1 <= nums2, move i, i+=1
    else, move j, j+=1
4. repeat step3 until move med steps

Time: O((m + n) / 2) 不符合题意
'''

import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        
        med = math.ceil((n1 + n2) / 2)
                
        i = 0
        j = 0
        step = 0
        res = 0

        while i < n1 and j < n2 and step < med:
            if nums1[i] <= nums2[j]:
                res = nums1[i]
                i += 1
                step += 1
            else:
                res = nums2[j]
                j += 1
                step += 1
                
        if (n1 + n2) % 2 == 1:
            
            if step == med:
                return res
            else:
                while i < n1 and step < med:
                    res = nums1[i]
                    i += 1
                    step += 1
                while j < n2 and step < med:
                    res = nums2[j]
                    j += 1
                    step += 1
                return res
        
        else:
            if step == med:
                if i < n1 and j < n2:
                    if nums1[i] <= nums2[j]:
                        return (float(res) + float(nums1[i])) / 2
                    else:
                        return (float(res) + float(nums2[j])) / 2
                elif i < n1:
                    return (float(res) + float(nums1[i])) / 2
                else:
                    return (float(res) + float(nums2[j])) / 2
            else:
                while i < n1 and step < med:
                    res = nums1[i]
                    i += 1
                    step += 1
                while j < n2 and step < med:
                    res = nums2[j]
                    j += 1
                    step += 1

                if i < n1:
                    return (float(res) + float(nums1[i])) / 2
                else:
                    return (float(res) + float(nums2[j])) / 2


"""
- 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
- 这里的 "/" 表示整除
- nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
- nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
- 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
- 这样 pivot 本身最大也只能是第 k-1 小的元素
- 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
- 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
- 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find(k):
            i = 0
            j = 0
            
            while True:
                # corner case
                if i == n:  # i超出边界或者nums1是空
                    return nums2[j + k - 1]
                if j == m:
                    return nums1[i + k - 1]
                if k == 1:
                    return min(nums1[i], nums2[j])
                
                i_temp = min(i + k // 2 - 1, n - 1)  # 判断取k/2个数的时候，是否超过边界
                j_temp = min(j + k // 2 - 1, m - 1)
                pivot1 = nums1[i_temp]
                pivot2 = nums2[j_temp]
                if pivot1 <= pivot2:
                    k -= i_temp - i + 1
                    i = 1 + i_temp
                else:
                    k -= j_temp - j + 1
                    j = 1 + j_temp
                
        n = len(nums1)
        m = len(nums2)
        med = 0
        if (n + m) % 2 == 1:
            k = (n + m) // 2 + 1
            med = find(k)
        else:
            k = (n + m) // 2
            med = (find(k) + find(k + 1)) / 2
        
        return med