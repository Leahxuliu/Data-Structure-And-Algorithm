'''
给一个数组，可修改一个值，求由连续相同值组成的子序列的最大长度
'''
from collections import defaultdict
def count(arr):
    if len(arr) < 3:
        return len(arr)
    
    n = len(arr)

    left = 0
    res = 1
    count = 0
    diff = 0
    for right in range(1, n):
        if arr[right] != arr[right - 1]:
            count += 1
        
            if count >= 2:
                left = diff
                count -= 1
                diff = right
            else:
                arr[right] = arr[right - 1]
                diff = right
        
        res = max(res, right - left + 1)
    return max(res, right - left + 1)

            
arr = [1, 1, 0, 0, 1, 1, 2, 1]
print(count(arr))
