# 1. Binary Tree

## 1.1 基础

**Tree**

*  数的组成：node + edges

*  root
*  parent / child
*  A node with no child is called a **leaf**

### 1.1.1 Node的定义

**In python**

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```



### 1.1.2 复杂度

**BFS**

- time complexity: O(N)
  每一个数都遍历一边，所以是N
- space complexity: average: O(N); 极端情况: O(1); N: the widest breadth(width)
  - space = 最宽层里数的个数，最底层的个数是 N/2，这里的N是Node个数
  - 极端情况，每一层都只有一个数，一进一出，每次都只含一个数

**DFS**

- time complexity: O(N)
  每一个数都遍历一边，所以是N
- space complexity: average: O(logN); worst: O(N)；logN:the high of tree
  - 储存空间等于层数
  - 当每一层都只有一个数的时候（极端情况）：层数 = N



## 1.2 Traversals

![截屏2020-10-26 上午8.42.54](/Users/leah/Dropbox/Leetcode/CS61B/CS61B_Xu/notebook/graph/Tree.png)



### 1.2.1 Lever Order

* Visit top-to-bottom, left-to-right
* D-B-F-A-C-E-G

**In python**

```python
# 102. Binary Tree Level Order Traversal

'''
BFS 层次遍历
'''
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        res = []

        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(temp)
        
        return res

'''
DFS 层次遍历
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        def dfs(root, depth):
            # depth是0-based
            if not root:
                return
            
            if len(res) < depth + 1:
                res.append([root.val])
            else:
                res[depth].append(root.val)
            
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            return
        
        res = []
        dfs(root, 0)
        return res
```



### 1.2.2 Depth First Traversals

* preorder: root-left-right; D-B-A-C-F-E-G

  * 自上而下，先操作再遍历
  * 技巧：一侧一侧遍历，zigzag形
  * preorder的变形，root-right-left
    * 比如117的DFS就可以用preorder的变形

* inorder: left-root-right; A-B-C-D-E-F-G 

  * 如果tree是BST的话，就是从小到大排序
  * 直通到最右边，然后该node的root，再right

* postorder：left-right-root; A-C-B-E-G-F-D

  * 自下而上，先遍历后操作
  * 当作一个个的subtree来看，左边完了，右边，最后是root
  * 类似DP
    * dfs(left)的结果，dfs(right)的结果，当前root.value --> 新的结果

  

  **In python**

  **preorder**

  ```python
  # DFS
  class Solution:
      def preorderTraversal(self, root: TreeNode) -> List[int]:
          if not root:
              return []
          
          def DFS(root):
              if not root:
                  return 
              
              res.append(root.val)
              DFS(root.left)
              DFS(root.right)            
              return
          
          res = []
          DFS(root)
          return res
        
        
  # iteration
  class Solution:
      def preorderTraversal(self, root: TreeNode) -> List[int]:
          if not root:
              return []
          
          res = []
          stack = [root]
          
          while stack:
              curr = stack.pop()
              res.append(curr.val)
              if curr.right:
                  stack.append(curr.right)
              if curr.left:
                  stack.append(curr.left)
          return res
        
  ```

  

  **inorder**

  ```python
  # DFS
  class Solution:
      def inorderTraversal(self, root):
          if not root:
              return []
          
          def DFS(root):
              if not root:
                  return 
              
              DFS(root.left)
              res.append(root.val)
              DFS(root.right)
              return
  
          res = []
          DFS(root)
          return res
        
  # iteration
  class Solution:
      def inorderTraversal(self, root: TreeNode) -> List[int]:
          if not root:
              return []
          
          stack = []
          res = []
  
          while stack or root:
              while root:
                  stack.append(root)
                  root = root.left
              
              curr = stack.pop()
              res.append(curr.val)
  
              if curr.right:
                  root = curr.right
          return res
  
  ```

  

  **postorder**

  ```python
  # DFS
  class Solution:
      def postorderTraversal(self, root: TreeNode) -> List[int]:
          if not root:
              return []
          
          def DFS(root):
              if not root:
                  return 
              
              DFS(root.left)
              DFS(root.right)
              res.append(root.val)
              return
  
          res = []
          DFS(root)
          return res
        
  # iteration
  class Solution:
      def postorderTraversal(self, root: TreeNode) -> List[int]:
          if not root:
              return []
          
          res = []
          stack = [root]
  
          while stack:
              curr = stack.pop()
              res.append(curr.val)
  
              if curr.left:
                  stack.append(curr.left)
              if curr.right:
                  stack.append(curr.right)
          return res[::-1]
          
  ```

  

  **In java**

  ```Java
  public class Traversal {
      private class BSTNode {
          int key;
          BSTNode left;
          BSTNode right;
  
          BSTNode() {}
          BSTNode(int key) { this.key = key; }
          BSTNode(int key, BSTNode left, BSTNode right) {
              this.key = key;
              this.left = left;
              this.right = right;
          }
  
      }
  		
      // preorder
      public void preOrder(BSTNode x) {
          if (x == null) return;
          System.out.println(x.key);
          preOrder(x.left);
          preOrder(x.right);
      }
    
      // inorder
      public void inOrder(BSTNode x) {
          if (x == null) return;
          inOrder(x.left);
          System.out.println(x.key);
          inOrder(x.right);
      }
    
      // postorder
      public void postOrder(BSTNode x) {
        if (x == null) return;
          postOrder(x.left);
          postOrder(x.right);
          System.out.println(x.key);
      }
  }
  ```

  

### 1.2.3 自下而上与自上而下

核心是遍历方向！

* 首先要明确，函数返回值是什么

* 函数仅仅是遍历，还是返回改变tree之后的node

  * 如果仅仅是遍历，可以只是return

    ```python
    def dfs(root):
      xxxx
      xxxx
      dfs(root.left)
      dfs(root.right)
      return
    ```

  * 如果返回的是tree的root，那么常常除了操作以外，在遍历的时候如下

    ```python
    def dfs(root):
      xxxx
      xxxx
      root.left = dfs(root.left)
      root.right = dfs(root.right)
      return root
    
    # 或者 
    # 对原本的树进行操作
    def dfs(root):
      xxxx
      xxxx
      l = dfs(root.left)
      r = dfs(root.right)
      
      root.left = l
      root.right = r
      return root
    
    ```

    

* 自下而上： 

  * 先递归再操作
  * 能划分成一个个小的subtree
    * root.left = xxxxx, root.right = xxxx 然后return root
    * 如果要对树进行修改，对树进行修改的语句放在遍历语句之后 切记切记！！
      * 如果在遍历的时候就对树进行操作，会改变树的样子，出错，比如226题
    * 考虑函数的返回值
  * 类似DP
    * dfs(left)的结果，dfs(right)的结果，当前root.value --> 新的结果
  * 遍历方向是postorder

* 自上而下

  * 先操作再递归

  * 比如从root到leaf的路径

  * 遍历方向是preorder

    * 也可以是preorder的变形，root-right-left

    



## 1.3 构造树 与 序列化与反序列化

### 1.3.1 手动构造树

```python
'''
手动构造
'''
Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(3)

Node1.left = Node2
Node1.right = Node3

# 注意
Node5 = TreeNode(5)
Node6 = TreeNode(5)
# Node5 != Node6, 因为Node5与Node6储存的地址是不一样的

Node7 = Node8 = TreeNode(5)
#这种情况，Node7==Node8，因为两者储存地址是相同的


```



### 1.3.2 通过层次遍历来构造树

```python
def constructTree(nodeList):
    if nodeList == []:
        return None

    root = TreeNode(nodeList[0])    
    queue = deque()
    queue.append((root, 0))
    n = len(nodeList)

    while queue:
        curr, index = queue.popleft()
        left = index * 2 + 1
        right = index * 2 + 1
        
        if left < n:
            curr.left = TreeNode(nodeList(left))
            queue.append(curr.left)
        if right < n:
            curr.right = TreeNode(nodeList(right))
            queue.append(curr.right)
    return root
```



### 1.3.3 重构二叉树

- [105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [106. 从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
- [889. 根据前序和后序遍历构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)



### 1.3.4 序列化与反序列化



## 1.4 Depth



## 1.5 Path



## 1.6 xxx







## 1.7 错题集

### 226 反转树

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        r = self.invertTree(root.right)
        l = self.invertTree(root.left)
        
        root.left = r
        root.right = l
        return root


# wrong
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        
        return root

```



### 437 Path Sum III

* Prefix + DFS



### 用迭代实现三种DFS的遍历

* 144， 145， 94





# 2. Binary SearchTree





# 3. B-Tree



# 4. Rotating Tree



# 5. Red-Black Tree



# 6. Tire



# 7. Python

* res[i].insert(0, root.val)
* 因为pop(0)的复杂度是O(N),所以BFS不用list的pop(0), 而是用queue
* is 比较的是地址
* == 比较的是值
* index = inorder.index(preorder[0])
* inorder_info = {each:i for i, each in enumerate(inorder)}

