# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/15  
# @Author  : XU Liu
# @FileName: 1.Two Sum.py

'''
1. 题目类型：


2. 题目要求与理解：
    给了一组数，和target，找到两数相加等于target
    输出这两个数的位置

3. 解题思路：


4. 输出输入以及边界条件：
input: 
output: 
corner case: 

5. 空间时间复杂度
    

'''

'''
暴力解法
空间时间复杂度
空间：O(1)
时间：O(N**2)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return []
        
        n = len(nums)
        for i in range(n - 1):
            for j in range(i+1, n):  # 易错！！！ 不是i，n！！！
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []


'''
from 小丁
用哈希表以空间换取速度，将查找时间从 O (n) 降低到 O (1)

在进行迭代并将元素插入到哈希表的同时，我们还会回过头来检查表中是否已经存在当前元素所对应的目标元素。如果它存在，那我们已经找到了对应解，并立即将其返回。

注意：这里没有使用对撞指针，因为这里数组是无序的，而排序的时间复杂度为 O (nlogn)，所以不太划算。

时间复杂度：O (n)，我们只遍历了包含有 n 个元素的列表一次。在表中进行的每次查找只花费 O (1) 的时间。
空间复杂度：O (n)，所需的额外空间取决于哈希表中存储的元素数量，该表最多需要存储 n 个元素。
'''


'''
dict: key是nums[i],value是i
temp = target - nums[i]
如果temp在dict里面，说明有两个数相加等于target的情况
如果没有就继续把nums[i]保存到dict里
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums_dict:
                return [nums_dict[temp],i]  # 易错 
            else:
                nums_dict[nums[i]] = i