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



**前序+后序**

```python
#Time:  O(N**2)  index查找O(N), N*N
#Space: O(N) since we store the entire tree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        
        
'''
DFS的优化
Time:  O(N) 
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        
        def DFS(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            temp = preorder[pre_start]
            root = TreeNode(temp)
            mid = info[temp]

            # 先写头和尾，不需要改变或者只需要+-1的
            # 通过len(preorder) = len(inorder)来计算中间值， 即通过in_end - in_start = pre_end - pre_start来计算
            root.left = DFS(pre_start + 1, pre_start - in_start + mid, in_start, mid - 1)
            root.right = DFS(pre_start - in_start + mid + 1, pre_end, mid + 1, in_end)
            return root
        
        info = {each:i for i, each in enumerate(inorder)}
        return DFS(0, len(preorder) - 1, 0, len(inorder) - 1)
```



**中序+后序**

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:mid], postorder[0:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        return root

'''
优化
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder == []:
            return None
        
        def DFS(in_start, in_end, post_start, post_end):
            if in_start > in_end:
                return None
                
            temp = postorder[post_end]
            root = TreeNode(temp)
            mid = inorder.index(temp)

            root.left = DFS(in_start, mid - 1, post_start, mid - 1 - in_start + post_start)
            root.right = DFS(mid + 1, in_end, mid - 1 - in_start + post_start + 1,post_end - 1)
            return root
        
        info = {each:i for i, each in enumerate(inorder)}
        return DFS(0, len(inorder) - 1, 0, len(postorder) - 1)

```



**前序+后序**

```python
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

```



### 1.3.4 序列化与反序列化

* 297

```python
# 利用前序遍历
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
      
      # 以下代码是错误的
      # 易错
      # baktracking的时候，是自己append然后pop，list一直是同一个list
      # 传入参数list[1:]时，不再是本身的list，而是新的list，这一层里还是原本的list，所以left，right传入进去的list[1:]内容是一样的
      # 回溯和递归的本质区别是函数的传导
      def DFS(data):
        if data == []:
            return None
        
        if data[0] == 'None':
            return None
        
        root = TreeNode(data[0])
        root.left = DFS(data[1:])
        root.right = DFS(data[1:])
        return root
```

```python
# 利用后序
# 从后往前删元素
# 先right 再left
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
```

```python
# 利用层次遍历
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

```



## 1.4 Depth



## 1.5 Path

* 113 Path SumII
* 进去的root就是要处理的node

```python
# BFS
from collections import deque
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        queue = deque()
        queue.append((root, [], 0))
        res = []

        while queue:
            curr, path, sumPath = queue.popleft()
            path.append(curr.val)
            sumPath += curr.val

            if sumPath == sum and curr.left == None and curr.right == None:
                res.append(path[:])
            
            if curr.left:
                queue.append((curr.left, path[:], sumPath))
            if curr.right:
                queue.append((curr.right, path[:], sumPath))
        return res

# DFS
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        def DFS(root, path, sumPath):
            if root == None:
                return
            
            # 为了防止混淆
            # 写dfs的时候，最好不要写append
            # 而是DFS(root.left, path + [root.val], sumPath)
            # 这里写append，不写pop不错的原因是因为，在本层当中，改变后的path不会再被利用
            path.append(root.val)
            sumPath += root.val
            if root.left == None and root.right == None and sumPath == sum:
                res.append(path[:])

            DFS(root.left, path[:], sumPath)
            DFS(root.right, path[:], sumPath)
            return
        
        res = []
        DFS(root, [], 0)
        return res
      
      
# backtracking
# backtracking则append，pop（一个递归参数对应一个append和pop的写法最不容易出错）
# 这里是两个递归对应一个append和pop，是因为有到最底层，root.left是None，root.right是None，这样就相当于两次pop
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        def DFS(root, path, sumPath):
            if root == None:
                return
            
            path.append(root.val)
            sumPath += root.val
            if root.left == None and root.right == None and sumPath == sum:
                res.append(path[:])
            
            DFS(root.left, path, sumPath)
            DFS(root.right, path, sumPath)
            path.pop()
            sumPath -= root.val
            return
        
        res = []
        DFS(root, [], 0)
        return res
```



## 1.6 DFS与Backtracking

* 回溯和递归的本质区别是函数的传导
  * 参考113题
* **为了防止混淆，便于记忆，DFS不要用append，改变参数；backtracking则append，pop（一个递归参数对应一个append和pop的写法最不容易出错）**
* 为了面试和今后少混淆，尽量全部都写DFS，不行append pop

### 1.6.1 排列

* 46（没有重复的integer)
  - 元素相同，位置不同则不同
  - 每次可以选择除已经选择过的其他元素
    - for i in nums:
      if i not in path:
  - 有指定的个数，即需要排列的元素个数
  - 当path的长度等于元素个数时，加入res list
  - 例：[1,2,3]
    - [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```python
# Backtraking
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        def backtracking(per):
            if len(per) == len(nums):
                res.append(per[:])

            for i in nums:
                if i not in per:
                    per.append(i)
                    backtracking(per)
                    per.pop()
            
            return 
        
        res = []
        backtracking([])
        return res

# DFS
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return []

        def DFS(per):
            if len(per) == len(nums):
                res.append(per[:])

            for i in nums:
                if i not in per:
                    DFS(per + [i])
            
            return 
        
        res = []
        DFS([])
        return res

# 错误
# 虽然放入的时候，是浅层copy了， 但是这一层的list是append之后的了
# 取下一个值的时候，是根据这一层现有的状况进行判断的，不pop掉就不行
# 上面正确DFS写法，这一层的list是不发生改变的，传入下一层的参数发生改变
# 113题，tree的path，那一题， append写在外面不错的原因是，本层list发生改变，但是不影响之后的代码，因为改变之后的list没有再被用到
# 排列的话，本层的list是要多次使用的
# 下面错误代码，找[1,2,3]的组合时，输出的结果会是[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]

        def backtracking(per):
            if len(per) == len(nums):
                res.append(per[:])

            for i in nums:
                if i not in per:
                    per.append(i)
                    backtracking(per[:])
            
            return 

```

* 47 （有重复的integer)

<img src="/Users/leah/Dropbox/Leetcode/CS61B/CS61B_Xu/notebook/graph/截屏2020-12-31 下午3.27.28-9396103.png" alt="截屏2020-12-31 下午3.27.28" style="zoom:80%;" />

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums  == []:
            return []
        
        def backtacking(visited, per):
            if len(per) == len(nums):
                res.append(per[:])
                return
            
            for i in range(len(nums)):
                if visited[i] == 0:
                    if i > 0 and nums[i - 1] == nums[i] and visited[i - 1] == 1:
                        continue

                    visited[i] = 1
                    per.append(nums[i])
                    backtacking(visited, per)
                    per.pop()
                    visited[i] = 0
        
        nums.sort()
        visited = [0] * len(nums)
        res = []
        backtacking(visited, [])
        return res
```







### 1.6.2 组合

* 77
  * 元素相同，位置不同也相同
  * 下一次可以选择的范围是本次选择数之后的数
    - for i in range(start, len(nums))
  * 有指定的个数，即需要被组合元素的个数，题目中会单独给出k值
  * 当path的长度等于k时，加入res list
  * 例：从1到4里面选择2个数
    - [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]



### 1.6.3 子集

* 78
* 90
  * 若nums里有重复的数，先sort
  * 元素相同，位置不同也相同
    - for i in range(start, len(nums))
  * 子集里面的元素，无指定的个数
  * 每一次的path都可加入res list
  * 例：
    - 无重复数
      - 比如[1,2,3] --> [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
    - 有重复数
      - 比如[1,2,2] --> [[],[1],[1,2],[1,2,2],[2],[2,2]]



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



### 111. Minimum Depth of Binary Tree

* 单边树
* DFS易错
* 



### 113

```python
# 错误1
# 结果是[[5,4,11,2],[5,4,11,2],[5,8,4,5],[5,8,4,5]]，同一个path出现两次
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        def dfs(root, path, pathSum):
            if root == None:  # 错误原因，left是None，right也是None，输出结果的时候，就会重复
                if pathSum == sum:
                    res.append(path[:])
                return
            
            path.append(root.val)
            pathSum = pathSum + root.val
            dfs(root.left, path, pathSum)
            dfs(root.right, path, pathSum)
            path.pop()
            return
        
        res = []
        dfs(root, [], 0)
        return res

# 错误2
# 回溯
# 要么执行到最后一层（None层），要么每一个递归函数对应一个append和pop
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        
        def dfs(root, path, pathSum):
            if root == None:
                return
            
            path.append(root.val)
            pathSum = pathSum + root.val
            if root.left == None and root.right == None:
                if pathSum == sum:
                    res.append(path[:])
                    # return  这里不能有return，要有return了，path就会有没有及时被pop的时候
                    # 比如[5,4,8,11,null,13,4,7,2,null,null,5,1]的树，应该是[5,4,11,2]，但是会变成[5,4,11,7,2]

            dfs(root.left, path, pathSum)
            dfs(root.right, path, pathSum)
            pathSum = pathSum - root.val
            path.pop()
            return
        
        res = []
        dfs(root, [], 0)
        return res
```



### 236. Lowest Common Ancestor of a Binary Tree

* 不会

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return 
        
        def findRoot(root):
            if root == None:
                return False, False

            l1, l2 = findRoot(root.left)
            r1, r2 = findRoot(root.right)
            
            ans1, ans2 = False, False
            if l1 or r1 or root == p:
                ans1 = True
            if l2 or r2 or root == q:
                ans2 = True

            if ans1 and ans2:
                self.res = root
                ans1 = False
                ans2 = False
            return ans1, ans2

        self.res = TreeNode()
        findRoot(root)
        return self.res
        
```



# 2. Binary SearchTree

## 2.1 Insert

* 701

```python
# always insert at a leaf node!!! 也就是说，每一次插入在最底层的node
# DFS
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
            return root
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
            return root
          
# 切记以下是错误的
# 函数返回的是tree node
        if root.val < val:
            return self.insertIntoBST(root.right, val)
        if root.val > val:
            return self.insertIntoBST(root.left, val)
        
# BFS
from collections import deque
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        
        node = root
        queue = deque()
        queue.append(node)

        while queue:
            curr = queue.popleft()
            if curr.val < val:
                if curr.right == None:
                    curr.right = TreeNode(val)
                else:
                    queue.append(curr.right)
            if curr.val > val:
                if curr.left == None:
                    curr.left = TreeNode(val)
                else:
                    queue.append(curr.left)
        return root
```

* insert node的时候，都是加在leaf上，这样会导致height越来越大
* 通过Overstuffing来实现防止不平衡，详见B-Trees



## 2.2 Delet

* 450

```python
# Time complexity should be O(height of tree) 平均情况 O(logN) 最坏情况 O(N)
# Space O(logN)

class BST:
    def deleteNode(self, root, target):
        if not root:
            return None
        
        # 递归调用左子树，右边树保持动，对左边数进行修改
        if target < root.val:
            root.left = self.deleteNode(root.left, target)
        
        # 递归调用右子树
        if target > root.val:
            root.right = self.deleteNode(root.right, target)

        # 当前节点的val == target
        if target == root.val:
            # 当前节点的左右都不存在，删掉后该节点变None
            if root.left == None and root.right == None:
                root = None
            elif root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            else:
                root.val = self.findPre(root)
                root.left = self.deleteNode(root.left, root.val) 
        return root

    # 移动前驱点
    def findPre(self, root):
        # 被删除节点的左边数里面的最右边
        root = root.left
        while root.right:
            root = root.right
        return root.val

    # 移动后驱点
    def findSuc(self, root):  # find the smallest node of root right subtree
        root = root.right
        while root.left:
            root = root.left
        return root.val

```



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

