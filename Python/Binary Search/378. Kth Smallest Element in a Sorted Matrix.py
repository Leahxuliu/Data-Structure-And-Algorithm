
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
        def count(target):
            '''
            return the number of integers less or equal target
            '''
            i = len(matrix) - 1
            j = 0
            num = 0
            while i >= 0 and j < len(matrix[0]):
                if target >= matrix[i][j]:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num
        
        l = matrix[0][0]
        r = matrix[-1][-1]

        '''
        类似找无明确targe的模版
        比如找第8位，小于等于7的有7个，小于等于9的有9个，说明9是第八位和第九位
        '''
        while l <= r:
            mid = l + (r - l) // 2
            num = count(mid)
            '''
            不能等号直接输出
            比如[[1,5,9],[10,11,13],[12,13,15]], mid=14时, count(mid) = 8
            此时第八位不是14，而是14前一位
            '''
            if num == k:
                r = mid - 1
            elif num < k:
                l = mid + 1
            else:
                r = mid - 1
        return l
