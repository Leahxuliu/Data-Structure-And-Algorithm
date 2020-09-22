'''
类似leedcode里240
二维的二分搜索

但是返回值不是boolean而是题干定义的Pairlnt？？
'''

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix == []:  # corner case
        return False
    if matrix == [[]]:
        return False
    #if target == 0:
    #       return False

    i = len(matrix) - 1
    j = 0

    while i >= 0 and j <= len(matrix[0]) - 1:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j += 1
        else:
            i -= 1
    return False

print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],100))