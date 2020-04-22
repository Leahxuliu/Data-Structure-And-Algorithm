#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/22  
# @Author  : XU Liu
# @FileName: 108. Convert Sorted Array to Binary Search Tree.py


# binary tree文件夹里也有此题

class Solution:
    def sortedArrayToBST(self, nums):
        if nums == None:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root



class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == None:
            return
        
        l, r = 0, len(nums) - 1
        if l <= r:
            mid = l + (r - l) // 2

            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[mid + 1:])
            return root