'''
1448. 统计二叉树中好节点的数目

给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。

「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。

'''
# Definition for a BT node
class TreeNode:
    def __init__(self, x = 0):
        self.val = x
        self.left = None
        self.right = None

def goodNodes(root):
    if root == None:
        return 0
    
    def find(root, maxVal):
        if root == None:
            return 
        
        next_maxVal = maxVal
        if root.val >= maxVal:
            self.res += 1
            next_maxVal = root.val
        find(root.left, next_maxVal)
        find(root.right, next_maxVal)

        return 
    
    self.res = 0
    find(root, float('-inf'))
    return self.res
