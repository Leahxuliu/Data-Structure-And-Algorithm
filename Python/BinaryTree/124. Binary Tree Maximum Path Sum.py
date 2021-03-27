# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
错误
这样的话，不包含left到left的情况
只包含root到left的path
'''

from collections import defaultdict
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return None
        
        def find(root, sumPath):
            if root == None:
                return 
            
            sumPath += root.val
            pre = min(prefix.keys())
            if pre < 0 :
                self.res = max(self.res, (sumPath - pre))
            else:
                self.res = max(self.res, sumPath)
            
            prefix[sumPath] += 1
            find(root.left, sumPath)
            find(root.right, sumPath)
            if prefix[sumPath] > 1:
                prefix[sumPath] -= 1
            else:
                prefix.pop(sumPath)
            sumPath -= root.val
            return

        # key: sum of path; value: th number of times 
        prefix = defaultdict(int)
        prefix[0] = 1

        self.res = root.val
        find(root, 0)
        return self.res



'''
path是一个node到另一个node的路径长

    a
   / \
  b   c

思路：自下而上
先求出b，c的最大值，自然就可以知道a的最大值
对于a来讲，最大值的情况：1. b,c都选（b-a-c）；2. 只选b或者c；3. 都不选 （注意！不能是三个node端点）
之前node为负数的时候，最大和肯定就要想办法舍弃负值（max(0, x)）

'''

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # corner case
        if root == None:
            return 0
        
        def find(root):
            '''
            return root为根节点时，单侧的最大值,这样才能确保是点到点的path
            注意不是root为根节点时的最大值，这样会出现三个端点
            '''
            if root == None:
                return 0
            
            l = find(root.left)
            r = find(root.right)

            curr = max((root.val + l), (root.val + r), root.val)
            self.res = max(self.res, curr, (root.val + l + r))

            return curr

        # self.res的起始值不能是0！
        self.res = -float('inf')
        find(root)
        return self.res