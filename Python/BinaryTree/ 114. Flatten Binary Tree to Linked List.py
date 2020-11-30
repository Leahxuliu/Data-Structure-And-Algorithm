# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    1
   / \
  2   5
 / \   \
3   4   6


1 -> 2 -> 3 -> 4 -> 5 -> 6
pre-order的话，把left放到right时，就会丢失原本right的信息
解决方法是，把pre-order逆过来
依次遍历6 5 4 3 2 1，然后每遍历一个节点就将当前节点的右指针更新为上一个节点
这样就不会有丢失孩子的问题了，因为更新当前的右指针的时候，当前节点的右孩子已经访问过了。
而 6 5 4 3 2 1 的遍历顺序其实变形的后序遍历，遍历顺序是右子树->左子树->根节点。


'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root == None:
                return None
            
            helper(root.right)
            helper(root.left)
            root.right = self.pre
            root.left = None
            self.pre = root        
            return
        
        self.pre = None
        helper(root)
        return 


'''
迭代
    1
   / \
  2   5
 / \   \
3   4   6

//将 1 的左子树插入到右子树的地方
    1
     \
      2         5
     / \         \
    3   4         6        
//将原来的右子树接到左子树的最右边节点
    1
     \
      2          
     / \          
    3   4  
         \
          5
           \
            6
            
 //将 2 的左子树插入到右子树的地方
    1
     \
      2          
       \          
        3       4  
                 \
                  5
                   \
                    6   
        
 //将原来的右子树接到左子树的最右边节点
    1
     \
      2          
       \          
        3      
         \
          4  
           \
            5
             \
              6         
  
  ......


'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return 
        
        while root:
            if root.left == None:
                root = root.right
            else:
                # 找左子树最右边的节点
                pre = root.left
                while pre.right:
                    pre = pre.right
                
                # 把root.right连接到左子树最右边的节点（pre）
                pre.right = root.right
                # 把root.left连接到左子树上
                root.right = root.left
                # 左子树变成none
                root.left = None
                # 下一个节点
                root = root.right
        return


'''
自下而上
分成一个个subtree
左子树放到右子树的地方，原本的右子树接到左子树的最右边节点
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return 
        if root.left == None and root.right == None:
            return 

        # 本题这里只是为了遍历一个个的subtree 不存在遍历顺序的问题
        # self.flatten(root.right)
        # self.flatten(root.left)
        # 先right再left也是对的
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left == None:
            return 
            
        # find pre-node
        pre = root.left
        while pre.right:
            pre = pre.right
        
        # connect pre-node with root.right
        pre.right = root.right
        # move root.left to root.right 
        root.right = root.left
        root.left = None
        return 