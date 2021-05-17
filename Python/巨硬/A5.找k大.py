'''
4
找k大
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        def find(k, start1, start2):
            '''
            return the k-th largest number
            '''
            if start1 >= len(nums1):
                return nums2[start2 + k - 1]
            if start2 >= len(nums2):
                return nums1[start1 + k - 1]
            
            if k == 1:
                return min(nums1[start1], nums2[start2])

            target = k // 2
            new_s1 = min(len(nums1) - 1, start1 + target - 1)
            new_s2 = min(len(nums2) - 1, start2 + target - 1)
            
            if nums1[new_s1] <= nums2[new_s2]:
                k = k - (new_s1 - start1 + 1)
                return find(k, new_s1 + 1, start2)
            else:
                k = k - (new_s2 - start2 + 1)
                return find(k, start1, new_s2 + 1)

        target = (n + m) // 2
        if (n + m) % 2 == 0:            
            return (find(target, 0, 0) + find(target + 1, 0, 0)) / 2.0
        else:
            return find(target + 1, 0, 0) * 1.0



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_k(arr1, arr2, k):
            """find mid value"""
            i, j = 0, 0  
            m, n = len(arr1), len(arr2)

            while True:  # 一直运行
                if i == m:
                    return arr2[j + k - 1]  # 对j增加的，+号变-号
                if j == n:
                    return arr1[i + k - 1]
                if k == 1:  # 易错点
                    return min(arr1[i], arr2[j])

                i_temp = min(m - 1, i + k // 2 - 1)  # 易错点
                j_temp = min(n - 1, j + k // 2 - 1) # 对j增加的，+号变-号

                if arr1[i_temp] <= arr2[j_temp]:
                    k -= (i_temp + 1 - i)
                    i = i_temp + 1
                else:
                    k -= (j_temp + 1 - j)  # 有j的变化判断差值的，前后颠倒
                    j = j_temp + 1  # j向j_temp右侧挪动一位
                
        n = len(nums1)
        m = len(nums2)
        med = 0
        if (n + m) % 2 == 1:
            k = (n + m) // 2 + 1
            med = find_k(nums1, nums2, k)
        else:
            k = (n + m) // 2
            med = (find_k(nums1, nums2,k) + find_k(nums1, nums2, k + 1)) / 2
        
        return med