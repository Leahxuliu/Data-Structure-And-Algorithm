# -*- coding: utf-8 -*-
# @Time    : 3/04/2020  
# @Author  : XU Liu
# @FileName: constructTree2.py

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



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
                queue.append([node.left, left_index])
            if right_index < len(nodeList):
                node.right = TreeNode(nodeList[right_index])
                queue.append([node.right, right_index])
            
        return root

x = BT()
print(x.constructTree([1,2,3,4,5,6,7]))


        
