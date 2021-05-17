'''
一个sorted array，整数，要求输出缺失的数字。比如输入是[5,6,7,11,13]，输出8, 9, 10, 12
'''

def find_miss_integer(arr):
    '''
    param: sorted array
    return missing integers in a list
    '''

    if arr == []:
        return []
    
    minVal = arr[0]
    maxVal = arr[-1]
    if len(arr) == maxVal - minVal + 1:
        return []
    

    arr_set = set(arr)
    res = []
    for i in range(minVal, maxVal):
        if i not in arr_set:
            res.append(i)
    
    return res 

a = find_miss_integer([5,6,7,11,13])
print(a)

a = find_miss_integer([5,6,7])
print(a)

'''
空间复杂度: O(1)
'''

def find_lost_number(arr):
    if arr == []:
        return []
    
    res = []
    for i in range(1, len(arr)):
        if arr[i - 1] + 1 != arr[i]:
            num = arr[i - 1] + 1
            while num != arr[i]:
                res.append(num)
                num += 1
    return res
a = find_lost_number([5,6,7,11,13])
print(a)

a = find_lost_number([5,6,7])
print(a)

'''
若不是sorted arr 且0-n里面找缺失数字
'''

# LC 268
def find_lost_number(arr):
    if arr == []:
        return []
    
    arr.sort()
    res = []
    for i in range(1, len(arr)):
        if arr[i - 1] + 1 != arr[i]:
            num = arr[i - 1] + 1
            while num < arr[i]:
                res.append(num)
                num += 1
    return res


# for i, each in enumerate(arr):
#     res ^= i ^ each