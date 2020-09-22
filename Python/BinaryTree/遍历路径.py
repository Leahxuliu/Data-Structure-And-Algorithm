# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
# 不用回溯
# 每一个node对应一个path
# path的改变写在dfs()里面，作为新的一个参数

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, path):
            if root == None:
                return
            
            if root.left == None and root.right == None:
                path.append(root.val)
                path_all.append(path)
            
            dfs(root.left, path+[root.val])  # 每一个node对应一个path，不管其它node上的path怎么变，该node上的path是不会发生改变的
            dfs(root.right, path+[root.val])
        
        
        path = []
        path_all = []
        dfs(root, path)
        return path_all

'''
错误答案

class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, path):
            if root == None:
                return
            
            path += [root.val]  
            # 猜测：如果把path写在外面，也就是所有node公用一个path，只要一个node上的path发生改变，所有path都跟着改变，导致最后出来的结果都是最长的那一条，要解决此问题，需要用回溯？？？
            print(id(path))
            # id地址不变
            # 如果是path = path + [root.val]
            # id地址是发生改变的

            if root.left == None and root.right == None:
                path_all.append(path)

            dfs(root.left, path)
            dfs(root.right, path)
        
        path = []
        path_all = []
        dfs(root, path)
        return path_all

x = Solution()
print(x.binaryTreePaths(root))
'''

'''
疑惑点：
为什么path写在dfs里就是孤立
写在外面就是通用的path？？？

答案：
保存地址的问题
python里面的赋值是根据地址来的
可以用id()来检验

正确与错误答案的区别有两个地方：
1. path + [root.val] 与 path += [root.val]
    前者是 x = x + y，x 出现两次，必须执行两次，性能不好，合并必须新建对象 x，然后复制两个列表合并,属于复制/拷贝 
    后者 x += y，x 只出现一次，也只会计算一次，性能好，不生成新对象，只在内存块末尾增加元素， in-place change，属于共享引用

2. 错误答案里面
    先path += [root.val]
    再  dfs(root.left, path)
       dfs(root.right, path)
    dfs进去的path是同一个
'''

'''
改进
'''
class Solution:
    def binaryTreePaths(self, root):
        def dfs(root, path):
            if root == None:
                return
            
            path += [root.val]  
            # 如果把path写在外面，也就是所有node公用一个path，只要一个node上的path发生改变，所有path都跟着改变，
            # 导致最后出来的结果都是最长的那一条，要解决此问题，需要用回溯

            if root.left == None and root.right == None:
                path_all.append(path)

            dfs(root.left, path[:])  # copy list 关键点
            dfs(root.right, path[:])
        
        path = []
        path_all = []
        dfs(root, path)
        return path_all

x = Solution()
print(x.binaryTreePaths(root))

# 回溯法1
class Tree:
    def findPath(self, root):
        res = []
        def dfs(root, path):
            if not root:
                return
            
            path.append(root.val)
            if not root.left and not root.right:
                res.append(path[:])
                
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        
        dfs(root, [])
        return res

# 回溯法2
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return 
            
        def helper(root, path):
            if root.left == None and root.right == None:
                all_path.append('->'.join(path[:]))
                return all_path
                
            for node in (root.left, root.right):  # 从选择列表里面做选择
                if node:
                    path.append(str(node.val))  # 执行
                    helper(node, path)  # 下一层的选择
                    path.pop()  # 撤销选择
                
        all_path = []
        helper(root, [str(root.val)])  # root是第一层（选择root作为第一层，有且只有一个选择）
        return all_path

# BFS
from collections import deque
class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if root == None:
            return []
        
        queue = deque()
        path = []
        path_all = []
        queue.append([root, path])

        while queue:
            node, path = queue.popleft()
            path.append(node.val)

            if node.left == None and node.right == None:
                path_all.append(path)

            if node.left != None:
                queue.append([node.left, path[:]])
            if node.right != None:
                queue.append([node.right, path[:]])
        return path_all

