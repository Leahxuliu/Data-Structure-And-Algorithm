class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) <= 1:
            return arr1
        if len(arr2) == 0:
            arr1.sort()
            return arr1
        
        info = {}
        lst = []
        arr2Set = set(arr2)
        for i in arr1:
            if i not in arr2Set:
                lst.append(i)
            else:
                if i in info:
                    info[i] += 1
                else:
                    info[i] = 1
        
        res = []
        for i in arr2:
            res += [i] * info[i]
        
        lst.sort()
        return res + lst



# 计数排序
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        upper = max(arr1)
        count = [0] * (upper + 1)

        for i in arr1:
            count[i] += 1
        
        res = []
        for i in arr2:
            res.extend([i] * count[i])
            count[i] = 0
        
        for i in range(len(count)):
            if count[i] != 0:
                res.extend([i] * count[i])
                count[i] = 0
        
        return res