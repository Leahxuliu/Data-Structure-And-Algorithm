#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
递归
自上往下再向上
自上往下: 分割成小部分（分割成1个数1个数）
自下再往上: 合并排序
'''

class SortList:
    def mergeSort(self, arr):
        n = len(arr)

        if n == 0:
            return []
        if n == 1:
            return arr

        # if n >= 2
        # divide the array elements into 2 lists
        mid = n // 2  
        L = arr[:mid]
        R = arr[mid:]

        # 递归划分
        # 划分成小部分，先到最底层，然后对最底层进行合并排序操作，然后再返回上一层接着合并排序操作
        L = self.mergeSort(L)  # Sorting the first half
        R = self.mergeSort(R)  # Sorting the second half

        # 合并
        # input: 两个已排序的list，L，R
        # 过程: 对L，R进行合并排序
        # output: 合并完成后的一个list
        i, j, k = 0, 0, 0  # i是L里面的指针，j是R里面的指针，k是这一轮arr里面的指针
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

            # 是否具有稳定性取决于L[i] == R[i]的时候，arr[k] = L[i]还是arr[k] = R[j], 前者具有稳定性，后者不具有稳定性
            # 稳定性: 同样大小的数值，保持其原有的顺序
            # 例: [5,4(a),4(b),3,2], 排序后: [2,3,4(a),4(b),5]

        # L或R有没有用完的情况，也就是两者len不同的时候
        if i < len(L):
            arr[k:] = L[i:]  # 在while最后,k，i，j都+1了
        
        if j < len(R):
            arr[k:] = R[j:]

        return arr



'''
迭代
自下往上
从两个数开始比, 然后合并
2个数,4个数,8,16....
'''
class SortList2:
    def mergeSort2(self, nums):
        n = len(nums)

        if n == 0:
            return []
        if n == 1:
            return nums

        # 排序
        def subSort(nums1, nums2):  # merge and sort two sorted list nums1 and nums2
            if not nums1:
                return nums2
            if not nums2:
                return nums1

            i, j = 0, 0
            res = []
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1

            if i < len(nums1):
                res.extend(nums1[i:])
            if j < len(nums2):
                res.extend(nums2[j:])
            return res
        

        # 划分成小部分
        # [5, 4, 2, 2, 1]
        # image: 
        # [5, 4] [2, 2] [1] --> [4, 5] [2,2] [1]
        # [2, 2, 4, 5] [1]

        interval = 1
        while interval < n:
            for i in range(0, n, 2 * interval):
                nums[i:i + 2 * interval] = subSort(nums[i:i + interval], nums[i + interval: i + 2 * interval])
            interval *= 2
        return nums

X = SortList2()
print(X.mergeSort2([2,2,3,8,45,21,11,3,10]))