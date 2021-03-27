# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
暴力解法
backtracking
1. root: select one of value in n 
2. build the tree
'''
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # cornor case
        if n == 0:
            return None
        if n == 1:
            return [TreeNode(1)]
        
        def copyTree(root):
            if root == None:
                return None
            
            new = TreeNode(root.val)
            new.left = copyTree(root.left)
            new.right = copyTree(root.right)
            return new 

        def insert(root, val):
            if root == None:
                return TreeNode(val)
            if val > root.val:
                root.right = insert(root.right, val)
            elif val < root.val:
                root.left = insert(root.left, val)
            return root
        
        def traversal(root, path):
            if root == None:
                path.append(0)
                return path
            path.append(root.val)
            traversal(root.left, path)
            traversal(root.right, path)
            return path
        
        def backtracking(root, used):
            '''
            pick a val and build the tree
            '''
            if len(used) == n:
                path = traversal(root, [])
                if path not in had:
                    had.append(path)
                    res.append(root)
                return
            
            for i in range(1, n + 1):
                if i not in used:
                    pre = copyTree(root)
                    insert(root, i)
                    used.append(i)
                    backtracking(root, used)
                    used.pop()
                    root = pre
            return

        res = []
        had = []
        for i in range(1, n + 1):
            root = TreeNode(i)
            backtracking(root, [i])
        return [each for each in res]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
利用BST的性质
可选的根节点[1...n]
当1是根节点的时候，[ ] 左子树，[ 2 ... n ] 右子树
把每个数字作为根节点，然后把所有可能的左子树和右子树组合起来
'''
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(n)]

        def find(start, end):
            '''
            返回的是所有可能性
            '''
            res = []
            # eg start:1, end:0 
            if start > end:
                return [None]
            # only one choose
            if start == end:
                return [TreeNode(start)]
            
            for i in range(start, end + 1):
                left = find(start, i - 1)
                right = find(i + 1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l 
                        root.right = r 
                        res.append(root)
            return res
        
        return find(1, n)
        