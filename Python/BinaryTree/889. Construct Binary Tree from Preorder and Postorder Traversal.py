# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if pre == []:
            return None
        
        root = TreeNode(pre[0])
        if len(pre) > 1:
            mid = post.index(pre[1])

            root.left = self.constructFromPrePost(pre[1:mid + 2], post[:mid + 1])
            root.right = self.constructFromPrePost(pre[mid + 2:], post[mid + 1:len(post) - 1])
        
        return root

'''
优化
'''
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if pre == []:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        
        def DFS(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            if pre_start == pre_end:
                return TreeNode(pre[pre_start])

            root = TreeNode(pre[pre_start])
            mid = post.index(pre[pre_start + 1])

            root.left = DFS(pre_start + 1, mid - post_start + pre_start + 1, post_start, mid)
            root.right = DFS(mid - post_start + pre_start + 2, pre_end, mid + 1, post_end - 1)
            
            return root
        
        info = {each:i for i, each in enumerate(post)}
        return DFS(0, len(pre) - 1, 0, len(post) - 1)
