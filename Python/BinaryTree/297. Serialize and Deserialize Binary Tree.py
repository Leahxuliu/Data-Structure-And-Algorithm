# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 前序遍历
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            return [root.val] + preorder(root.left) + preorder(root.right) if root else ['None']
        return ','.join(map(str, preorder(root)))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        def constructor(data):
            val = int(data.pop(0))
            if val == 'None':
                return None
            
            root = TreeNode(val)
            root.left = constructor(data)
            root.right = constructor(data)
            return root
        return constructor(data)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# 后序遍历
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''
        
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else ['None']
        return ','.join(map(str, postorder(root)))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        data = data.split(',')
        def helper(data):
            val = data.pop()
            if val == 'None':
                return None
            
            root = TreeNode(val)
            root.right = helper(data)
            root.left = helper(data)
            return root
        return helper(data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# BFS

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''

        res = []
        queue = deque()
        queue.append(root)
        res.append(root.val)
        while queue:
            node = queue.popleft()
            if node == 'None':
                continue
            if node.left != None:
                queue.append(node.left)
                res.append(node.left.val)
            else:
                res.append('None')
            if node.right != None:
                queue.append(node.right)
                res.append(node.right.val)
            else:
                res.append('None')
        # print(','.join(map(str, res)))
        return ','.join(map(str, res))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None

        data = data.split(',')
        root = TreeNode(data.pop(0))
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            # build left
            val = data.pop(0)
            if val != 'None':
                node.left = TreeNode(val)  # 易错 不是val，而是Treenode(val)
                queue.append(node.left)  # should be add
            
            # build right
            val = data.pop(0)
            if val != 'None':
                node.right = TreeNode(val)
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))