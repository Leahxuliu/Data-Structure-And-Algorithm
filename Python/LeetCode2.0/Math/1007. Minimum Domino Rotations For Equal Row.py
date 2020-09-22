'''
Method - brute force
Steps:
    1. create a set (info), put set(A) and set(B) into info
    2. scan info (each_num)
        check can all the values in A or B are each_num
    3. if no case in step2, return -1
       else, choose the min times
       
Time: O(N**2)

Modify
1. create a info dict, key: integer, value:[the number of this integer in A, B]
2. scan info
    if value[0] + value[1] < len(A), continue
    else,
        if value[0] > value[1], find the number of rotations that all values in A are the same
        else, find the number of rotations that all values in B are the same
3. return min

Time: O(N + N + N + N) = O(N)
Space: O(N)
'''

from collections import defaultdict
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        temp = set(A + B)
        info = defaultdict(list)
        
        for m in temp:
            info[m].append(A.count(m))
            info[m].append(B.count(m))
        
        def rotation(l1, l2, target, n):  # all values in l1 are target
            i, j = 0, 0
            count = 0
            while i < n and j < n:
                if l1[i] == target:
                    i += 1
                    j += 1
                elif l1[i] != target:
                    if l2[i] == target:
                        count += 1
                        i += 1
                        j += 1
                    else:
                        return -1
            return count
        
        n = len(A)
        min_res = float('inf')
    
        for k, v in info.items():
            if v[0] + v[1] >= n:
                if v[0] > v[1]:  # B --> A
                    res = rotation(A, B, k, n)
                    if res != -1:
                        min_res = min(min_res, res)
                else:
                    res = rotation(B, A, k, n)
                    if res != -1:
                        min_res = min(min_res, res)
        if min_res != float('inf'):
            return min_res
        else:
            return -1
            