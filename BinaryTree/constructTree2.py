# -*- coding: utf-8 -*-
# @Time    : 3/04/2020  
# @Author  : XU Liu
# @FileName: constructTree2.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''from collections import deque
class BT:
    def constructTree(self, nodeList):  # input: list using bfs, output: root
        if not nodeList:  # corner case
            return None

        res = root = TreeNode(nodeList[0])
        queue = deque([(root, 0)])
        while queue:
            root, ind = queue.popleft()
            l_ind = ind * 2 + 1
            r_ind = ind * 2 + 2
            if l_ind < len(nodeList):  # judge if left or right exist
                root.left = TreeNode(nodeList[l_ind])
            if r_ind < len(nodeList):
                root.right = TreeNode(nodeList[r_ind])
            if root.left:
                queue.append([root.left, ind * 2 + 1])
            if root.right:
                queue.append([root.right, ind * 2 + 2])
        return res'''

from collections import deque
class BT:
    def constructTree(self, nodeList):
        if not nodeList:  # corner case
            return None
    
        root = TreeNode(nodeList[0])
        queue = deque([(root, 0)])
        while queue:
            node, index = queue.popleft()
            left_index = index * 2 + 1
            right_index = index * 2 + 2
            if left_index < len(nodeList):
                node.left = TreeNode(nodeList[left_index])
                if node.left != None:
                    queue.append([node.left, left_index])
            if right_index < len(nodeList):
                node.right = TreeNode(nodeList[right_index])
                if node.right != None:
                    queue.append([node.right, right_index])
            
        return root

x = BT()
print(x.constructTree([1,2,3,4,5,6,7]))