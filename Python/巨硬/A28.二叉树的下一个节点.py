'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey

'''

# 1.右边的最左节点；2.右上节点

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None
        
        if pNode.right:
            curr = pNode.right
            while curr.left:
                curr = curr.left
            return curr
        

        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
            
        return None