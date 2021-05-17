'''
判断一个数组是否是大约排好序的，也就是满足下面两个条件的其中一个即可

1. 交换任意两个数字，得到的是一个排好序的比如[1,5,3,4,2]
2. 数组中的一段子序列旋转后能是一个排好序的数组，比如[1,2,7,6,5,4,3,8,9],旋转[7,6,5,4] 

（假设是升序数组, 假设无重复）
'''


'''
核心：找下降

1. 判断是不是sorted arr
2. 下降的地方是不是一串连续的
3. 下降的地方是不是两对pair
'''

def checksorted(arr):
    if arr == []:
        return True
    
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True

def rotated(arr):
    # 下降的地方有且只有一个
    
    flag = False
    i = 1
    n = len(arr) - 1
    while i < n:
        if arr[i] > arr[i - 1]:
            i += 1
        else:
            if flag:
                return False

            flag = True 
            start = i - 1
            while i < n and arr[i] < arr[i - 1]:
                i += 1
            if arr[start] >= arr[i] or arr[i - 1] <= arr[start - 1]:
                return False
            
    return flag

def checkswap(arr):
    pairs = []
    i = 1
    n = len(arr)

    while i < n:
        if arr[i] < arr[i - 1]:
            pairs.append([i - 1, i])
        i += 1
    
    if len(pairs) == 1:
        i, j = pairs[0]

        if arr[i] < arr[j + 1] and arr[j] > arr[i - 1]:
            return True

    elif len(pairs) == 2:
        i1, j1 = pairs[0]
        i2, j2 = pairs[1]

        if arr[j1] > arr[j2] and arr[i1] > arr[i2]:
            return True

    return False





if __name__ == '__main__':
    # arr = [1, 5, 3, 4, 2]
    # arr = [1,2,7,6,5,4,3,8,9]
    # arr = [4,3,2,8,9]
    # arr = [1,2,7,6,5,4]
    # arr = [1,10, 2, 3]
    # arr = [1,2,5,4,3]  # true
    # arr = [1, 5, 3, 4, 2]  # true
    # arr = [1,5,4,3,2,6, 8, 7, 9]  # false
    # arr = [1,2,3,4]  # true
    # arr = [1,2,3,9,5,8]  # false
    arr = [1,5,4,3,2,6]  # true

    flag = False
    arr = [float('-inf')] + arr + [float('inf')]

    # check if sorted or not
    if checksorted(arr):
        print('sorted')
        flag = True
    
    # check if rotated
    elif rotated(arr):
        print('rotated')
        flag = True
    
    # swap two nums --> sorted?
    elif checkswap(arr):
        print('swap')
        flag = True
    
    print(flag)
