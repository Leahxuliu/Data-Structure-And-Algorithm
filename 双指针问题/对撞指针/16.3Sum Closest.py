# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/15  
# @Author  : XU Liu
# @FileName: 16.3Sum Closest.py

'''
1. 题目类型：


2. 题目要求与理解：


3. 解题思路：
    step1. sort数组
    step2. 利用15题的方式，枚举每一中可能的和
    step3. 利用二分搜索，找到最接近target的和

4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''


'''
二分搜索写错了 待修改
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        all_res = set()
        
        n = len(nums)
        for i in range(n):
            # 这一个数跟上一个 数一样，上一轮已经考虑过了，去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l = i + 1
            r = n - 1
            
            while l < r:  # 不用等号
                temp = nums[i] + nums[l] + nums[r]
                if temp > target:
                    r -= 1
                    all_res.add(temp)
                elif temp < target:
                    l += 1
                    all_res.add(temp)
                elif temp == target: 
                    return target
                
        def BT(nums, T):
            l, r = 0, len(nums) - 1
            
            while l <= r:
                mid = l + (r - l) // 2
                
                if nums[mid] > T:
                    r = mid - 1
                elif nums[mid] < T:
                    l = mid + 1
            if r > 0 and abs(nums[l] - T) > abs(nums[r] - T):
                return nums[r]  # 易错 不是l是nums[l]
            else:
                return nums[l]

        if len(all_res) == 1:  # 易忘记 all_res里面可能就一种情况
            return list(all_res)[0]
        else:
            all_res = sorted(list(all_res))
            res = BT(all_res, target)
            return res


'''
方法2
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        a = float('inf')
        res = 0

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                # 比较sums与目标target的距离与之前最近的距离，如果更近则更新
                if abs(sums-target) < a:
                    a = abs(sums-target)
                    res = sums
                
                if sums > target:
                    right -= 1
                elif sums < target:
                    left += 1
                # 如果sums == target，则说明距离为0，这就是最接近的数
                elif sums == target:
                    return sums
        return res