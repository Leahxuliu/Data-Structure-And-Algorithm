#!/usr/bin/python
# -*- coding: utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import constructTree
class BST:
    def deleteNode(self, root, target):
        if not root:
            return None
        
        # 递归调用左子树，右边树保持动，对左边数进行修改
        if target < root.val:
            root.left = self.deleteNode(root.left, target)
        
        # 递归调用右子树
        if target > root.val:
            root.right = self.deleteNode(root.right, target)

        # 当前节点的val == target
        if target == root.val:
            # 当前节点的左右都不存在，删掉后该节点变None
            if root.left == None and root.right == None:
                root = None
            # 当前节点的左节点不存在，直接提升右节点
            elif root.left == None:
                root = root.right
            # 当前节点的右节点不存在，直接提升左节点
            elif root.right == None:
                root = root.left
            # 当前节点的左右都存在，用被删除节点的前驱节点（即比被删除节点小一位的节点） 代替
            else:
                root.val = self.findPre(root)
                root.left = self.deleteNode(root.left, root.val)  # 原本的left数发生了改变，要重新排，同时也意味着要删掉被上挪的节点
                '''
                root.val = self.findSuc(root)
                root.right = self.deleteNode(root.right, root.val)
                '''
        return root

    # 移动前驱点
    def findPre(self, root):
        # 被删除节点的左边数里面的最右边
        root = root.left
        while root.right:
            root = root.right
        return root.val

    # 移动后驱点
    def findSuc(self, root):  # find the smallest node of root right subtree
        root = root.right
        while root.left:
            root = root.left
        return root.val


if __name__ == '__main__':
    root = constructTree.constructTree([5,20,None,50,None,66,68,75,80,90,150])
    result = BST()
    print(result.deleteNode(root, 50))