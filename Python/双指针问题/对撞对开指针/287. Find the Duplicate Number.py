# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/20

# hash
# time complexity: O(n)
# space complexity:O(n)
from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        info = defaultdict(int)
        for i in nums:
            info[i] += 1
            if info[i] > 1:
                return i


# tow pointer fast and slow
# time complexity: O(n)
# space complexity:O(1)
'''
[数值, index]为一对pair, 数值 -> 数值对应的index -> 数值 -> 数值对应的index
（能找到两个不同的索引（但是值相等）指向同一索引，这就成环）
类似链表里面找环的交点
setp1: slow走一步, fast走两步, 找到相遇点
    slow = nums[slow], fast = nums[nums[fast]]
step2: i从step1的交点出发，j从0（index）出发，i与j相遇的点就是环的起点，也就是重复数

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 0
        f = 0
        
        while (1):
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        s = 0
        while s != f:
            
            s = nums[s]
            f = nums[f]
        
        return s