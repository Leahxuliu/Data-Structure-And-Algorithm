#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
若布局良好，则是O(log(n)) 也就是树的高度
若是skewed tree，node分布在一条直线上，查找时间为 O(n) worst case
'''


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BST:
    def findBFS(self, root, target):
        if not root:
            return None
        
        while root:
            if root.val == target:
                return root
            elif root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
        return None
    
    def findDFS2(self, root, target):
        if not root:
            return None
        if root.val == target:
            return root
        
        if target < root.val:
            return self.findDFS2(root.left, target)
        else:
            return self.findDFS2(root.right, target)
    

if __name__ == "__main__":
    Node1 = TreeNode(4)
    Node2 = TreeNode(1)
    Node3 = TreeNode(6)
    Node4 = TreeNode(5)
    Node5 = TreeNode(8)

    Node3.left = Node4
    Node3.right = Node5
    Node1.left = Node2
    Node1.right = Node3
    
    # print(Node1)
    root = Node1
    x = BST()
    print(x.findDFS2(root,5))
