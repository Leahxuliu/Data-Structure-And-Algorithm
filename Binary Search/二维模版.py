# 模板1
# 二维矩阵的数是从前往后，从上往下，且i行尾< i+1行头的
# 当作一维array进行二分搜索
def searchMatrix(matrix, target):
    row = len(matrix)
    columns = len(matrix[0])
    
    l, r = 0, row * column - 1
    while l <= r:
        mid = l + (r - l) // 2
        midVal = matrix[mid // column][mid % column]  #行，列
        if target == midVal:
            return True
        if target < midVal:
            r = mid - 1
        else:
            l = mid + 1
    return False


# 模板2
# 二维矩阵的数是从前往后，从上往下，且每行都是独立增长的
# 进行对角线搜索 diagonal search： 从左上到右下遍历i，然后对i的行和列进行二分搜索
class Matrix
    def searchMatrix(self, matrix, target):
        # corner case

        for i in range(min(len(matrix), len(matrix[0]))):
            r = self.binarySearch(i, matrix, target, 1)  # 1 represent search the row
            c = self.binarySearch(i, matrix, target, 0)
            if r or c:
                return True
        return False
    
    def binarySearch(self, i, matrix, target, tag):  # return True if having target
        m = len(matrix)
        n = len(matrix[0])
        
        
        l = i
        if tag == 1:
            r = n - 1  # 别忘记 - 1
        else:
            r = m - 1
        
        
        while l <= r:
            mid  = l + (r - l) // 2
            if tag == 1:
                midVal = matrix[i][mid]
            else:
                midVal = matrix[mid][i]
            if midVal == target:
                return True
            elif midVal < target:
                l = mid + 1
            else:
                r = mid - 1
        return False