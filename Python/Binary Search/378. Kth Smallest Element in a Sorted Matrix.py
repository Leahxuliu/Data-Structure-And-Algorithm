# 错误
'''
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

对目标值进行二分的时候
如果用常规模版，那么mid=14的时候，find(14) = 8
答案就会是14，可是14并不存在于matrix里面
所以当find(target) = k的时候，这里的target不一定是答案，需要进一步缩小
类似找到第一个target值
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def find(target):
            n = len(matrix)
            i = n - 1
            j = 0
            num = 0

            while i >= 0 and j < n:
                if matrix[i][j] <= target:
                    num += i + 1  # don't forget +1
                    j += 1
                else:
                    i -= 1
            return num
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l <= r:
            mid = l + (r - l) // 2
            num = find(mid) 
            print(mid, num)
            if num == k:
                return mid
            if num < k:
                l = mid + 1
            else:
                r = mid - 1
        return -1

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        def find(target):
            n = len(matrix)
            i = n - 1
            j = 0
            num = 0

            while i >= 0 and j < n:
                if matrix[i][j] <= target:
                    num += i + 1  # don't forget +1
                    j += 1
                else:
                    i -= 1
            return num
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l <= r:
            mid = l + (r - l) // 2
            num = find(mid) 
            if num >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l
