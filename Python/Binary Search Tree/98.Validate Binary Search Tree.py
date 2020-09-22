# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/03  
# @Author  : XU Liu
# @FileName: 98.Validate Binary Search Tree.py

'''
1. 题目类型：
    BST

2. 题目要求与理解：
    判断给到的树是不是BST

3. 解题思路：
    方法一：递归(由上至下)
    易错点：只判断node.right.val > node.val 和 node.left.val < node.val是不充分的
           因为不仅右子结点要大于该节点，整个右子树的元素都应该大于该节点
    解决方案：遍历树的同时保留结点的上界与下界，在比较时不仅比较子结点的值，也要与上下界比较
    Node.left可以无限小，但是不能比node以及node之上的数大

    方法二：中序遍历
    中序遍历按照左子树 -> 结点 -> 右子树的顺序，这意味着一个二叉搜索树的中序遍历得到的每个元素都应该比下一个元素小
    a. 计算中序遍历列表 inorder
    b. 检查中序遍历列表是否从小到大

4. 输出输入以及边界条件：
input: root: TreeNode
output: bool
corner case: None

5. 空间时间复杂度
    time complexity order: O(N)
    space complexity order: O(H) = O(logN)

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 方法一
    def isValidBST(self, root):
        def helper(root,max_val,min_val):
            if root == None:
                return True

            if root.val < max_val and root.val > min_val:
                return helper(root.left,root.val,min_val) and helper(root.right,max_val,root.val)
            return False

        max_val = float('inf')
        min_val = -float('inf')
        return helper(root,max_val,min_val)

    # 方法二
    def isValidBST2(self, root):
        if root == None:
            return True

        pre = -float('inf')
        stack = []
        p_node = root

        # p_node是None，意味着这这一侧已经是最左边了，且这个最左边的node没有right，要往上层的right走
        # stack == [], 刚开始的时候或者root.left都比完了(包括root)，要开始比root.right
        while stack or p_node:
            # 把所有当前访问节点的左孩子都入栈
            while p_node:
                stack.append(p_node)
                p_node = p_node.left

            # 操作栈顶节点，如果是第一次运行到这步，那么这是整棵树的最左节点
            cur_node = stack.pop() 
            # 检查是否从小到大
            if cur_node.val > pre:
                pre = cur_node.val
            else:
                return False

            # 将指针指向当前节点的右节点
            if cur_node.right != None:
                p_node = cur_node.right

        return True


if __name__ == "__main__":
    Node1 = TreeNode(5)
    Node2 = TreeNode(1)
    Node3 = TreeNode(4)
    Node4 = TreeNode(3)
    Node5 = TreeNode(6)

    Node3.left = Node4
    Node3.right = Node5
    Node1.left = Node2
    Node1.right = Node3
    
    # print(Node1)
    root = Node1
    print(root)
    x = Solution()
    print(x.isValidBST(root))

