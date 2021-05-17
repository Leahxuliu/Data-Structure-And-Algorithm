'''
给一个数组，数字是有序的，其中缺失1个数，输出这个数 （连续的一段，但不一定是1-N）
    进阶1: 如果缺失了多个数，输出所有缺失的数字
    进阶2: 如果只需要求缺失了多少个数字呢？

给一个数组，数字是无序的，其中缺失1个数，输出这个数 （连续的一段，但不一定是1-N）


给一个数组，数字是1～N，N是数组的长度，无序的，缺失一个数，输出这个数


给一个数组，数字是1～N，N是数组的长度，有序的，缺失一个数，输出这个数


参考LC 268
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

LC 缺失的第一个正整数，41题

缺失的数，非连续，且无序
'''

'''
需要明确的条件：
1. interger大小的范围
2. 是否是有序的
3. 是否是空


if mid + 1 == arr[mid], the missing number is in [mid + 1 r], so move l to mid + 1
if mid + 1 != arr[mid], the missing number is in [l, mid], so move r to mid - 1
'''


# '''
# LC 268
# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
# '''


'''
给定一个包含 [1, n] 中 n - 1 个数的数组 nums ，找出 [1, n] 这个范围内没有出现在数组中的那个数。

n == nums.length + 1
1 <= n <= 10**4
1 <= nums[i] <= n
All the numbers of nums are unique.
'''

'''
方案一
1. set nums
2. traversal interger from 0 to N, check the interger is in nums or not
时间复杂度：O(2N)
空间复杂度：O(N)
'''
def missingNumber(nums):
    '''return the missing number
    Args:
        nums(list)
    Reture:
        int:the missing nuber
    '''
    nums_set = set(nums)

    for i in range(1, len(nums) + 2):
        if i not in nums_set:
            return i

'''
方案二
位运算里面的异或
时间复杂度：O(N)
空间复杂度：O(1)
'''
def missingNumber(nums):
    res = len(nums) + 1

    for i, each in enumerate(nums):
        res ^= (i + 1)
        res ^= each
    
    return res

'''
方案三
高斯求和
求和是不是有溢出的风险
时间复杂度：O(N)
空间复杂度：O(1)
'''
def missingNumber(nums):
    n = len(nums) + 1
    return (n + 1) * n // 2 - sum(nums)


'''
方案四
排序+二分
若是无序：
时间复杂度：O(NlogN + logN)
空间复杂度：O(1)

若是有序：
时间复杂度：O(logN)
空间复杂度：O(1)
'''
def missingNumber(nums):
    nums.sort()
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == mid + 1:
            l = mid + 1
        else:
            r = mid - 1
        
    return l + 1


# print(missingNumber([1,2,4,5,6]))
# print(missingNumber([1]))
# print(missingNumber([2]))
# print(missingNumber([1, 2, 3, 4]))

def missingNumber(nums, N):
    nums_set = set(nums)

    res = []
    for i in range(1, N + 1):
        if i not in nums_set:
            res.append(i)
    return res 

# print(missingNumber([1, 1, 2, 2, 4, 5, 6], 7))



def missingNumber(nums):
    nums.sort()
    if (nums[-1] - nums[0] + 1) == len(nums) and nums[0] == 1:
        return -1

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == mid + 1:
            l = mid + 1
        else:
            r = mid - 1
        
    return l + 1

# print(missingNumber([2, 3]))
# print(missingNumber([1, 2, 4]))
# print(missingNumber([1, 2, 3]))


'''
input: sorted arr
the value of intergers in arr: 1 ~ N
unique
N = len(arr) + 1

[1, 2, 3] -> missing 4 
[1, 2, 4] -> missing 3

binary search
time complexity: O(logN)
space complexity: O(1)

'''


def find_missing_number(arr):
    ''' return the missing number 
    Args:
        arr(list): sorted array 
    Return:
        int(integer)
    '''

    # corner case
    if arr == []:
        return 1
    
    # use binary search to find missing number
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == mid + 1:
            l = mid + 1
        else:
            r = mid - 1
    return l + 1

# arr = []
# print(find_missing_number(arr))  # except 1

# arr = [1, 2, 4]
# print(find_missing_number(arr))  # except 3

# arr = [1, 2, 3]
# print(find_missing_number(arr))  # except 4

# arr = [2, 3]
# print(find_missing_number(arr))  # except 1




def find_missing_number(arr):
    ''' return the missing number 
    Args:
        arr(list): unsorted array 
    Return:
        int(integer)
    '''

    # corner case
    if arr == []:
        return 1
    
    res = len(arr) + 1
    for i, each in enumerate(arr, 1):
        res ^= i 
        res ^= each 
    return res
    

# arr = []
# print(find_missing_number(arr))  # except 1

# arr = [1, 2, 4]
# print(find_missing_number(arr))  # except 3

# arr = [1, 2, 3]
# print(find_missing_number(arr))  # except 4

# arr = [2, 3]
# print(find_missing_number(arr))  # except 1


'''
缺失多个

input: sorted arr, N
1~N


[1, 2, 4], N = 6 --> [3, 4, 6]

[1, 2, 4], N = ? --> [3...?]


'''

def find_missing_number(arr, N):
    # corner case
    if arr == []:
        return [each for each in range(1, N + 1)]

    res = []
    j = 0
    n = len(arr) 
    for i in range(1, N + 1):
        if j < n and arr[j] == i:
            j += 1
            continue 
        
        res.append(i)
    return res 

arr = []
print(find_missing_number(arr, 2))  # except [1, 2]

arr = [1, 2, 4]
print(find_missing_number(arr, 4))  # except [3]

arr = [1, 2, 3]
print(find_missing_number(arr, 4))  # except [4]

arr = [2, 3]
print(find_missing_number(arr, 4))  # except [1, 4]
