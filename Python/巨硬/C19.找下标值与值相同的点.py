'''
有序数组找到num[i] == i的那个，进阶：数组有可能有重复值


1. 无
'''

def find(nums):
    if nums == []:
        return -1

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if mid == nums[mid]:
            return mid 
        elif mid < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1

a = find([-1,0,2,6])
print(a)
a = find([-1,0,3,6])
print(a)