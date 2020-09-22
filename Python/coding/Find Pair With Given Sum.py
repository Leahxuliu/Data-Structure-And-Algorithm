'''
Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
Example 2:

Input: nums = [20, 50, 40, 25, 30, 10], target = 90
Output: [1, 5]
Explanation:
nums[0] + nums[2] = 20 + 40 = 60 = 90 - 30
nums[1] + nums[5] = 50 + 10 = 60 = 90 - 30
You should return the pair with the largest number.

'''

def twoSum(nums, target):
    target -= 30
    max_num = 0
    res = []
    info = {}

    for i, n in enumerate(nums):
        temp = target - n
        if temp in info:
            if max_num < max(temp, n):
                res = [info[temp], i]
                max_num = max(temp, n)
        info[n] = i
    
    # 注意 没有pair的时候，return空list还是return[-1, -1]
    return res

print(twoSum([1, 10], 90))
    

