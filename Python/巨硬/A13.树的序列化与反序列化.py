# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        
        data = []

        def traversal(root):
            if root == None:
                data.append('#')
                return 
            
            data.append(str(root.val))
            traversal(root.left)
            traversal(root.right)
            return
        
        traversal(root)
        return ' '.join(data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        data = data.split(' ')[::-1]
        def build(root, data):
            nodeVal = data.pop()
            if nodeVal == '#':
                return None

            root = TreeNode(int(nodeVal))
            root.left = build(root.left, data)
            root.right = build(root.right, data)
            return root 
        
        
        return build(None, data)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))