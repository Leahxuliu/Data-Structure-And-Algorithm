'''
1. use binary search to find the index of x in arr (I)
    if x not in arr, return the index where should be
# 2. append arr[I-k:I+k] into heap
#     abs(arr[i] - x)
# 3. pop heap k times
#     last time should check whether same diff in heap
2. sliding window

'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr == []:
            return []
        
        def find(target):
            l = 0
            r = len(arr) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            if r < 0:
                return 0
            if l >= len(arr):
                return len(arr) - 1
            
            return l if abs(arr[l] - target) < abs(arr[r] - target) else r  # 易错，这里没有等号

        # find x
        index = find(x)

        # 固定窗口
        left = max(0, index - k + 1)
        right = left + k - 1

        while right + 1 < len(arr):
            if abs(arr[right + 1] - x) < abs(arr[left] - x):
                right += 1
                left += 1
            else:
                break
    
        return arr[left: right + 1]
        
        



'''
对撞双指针
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr == []:
            return []
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            return arr[-k:]
        
        l = 0
        r = len(arr) - 1

        while r - l + 1 != k:
            if x - arr[l] <= arr[r] - x:
                r -= 1
            else:
                l += 1

        return arr[l:r + 1]