# 1 知识点

## 1.1 基础知识

* 这里的graph都是指simple graph
  * 没有AB，BA
  * 没有AA，自己到自己

- 顶点: vertex, a.k.a. node; 边: edge

  - vertices with an edge between are adjacent
  - Optional: Vertices or edges may have labels (or weights)

- 图的表示

  - 邻接表(**adjacent table**)：每个节点的邻接点的总集合

    - 时间复杂度：O(V + E)
    - 用list表示，例如：[[1],[2],[3]]，0指向1，1指向2，2指向3
    - 用dict表示，例如：{0:[1], 1:[2], 2:[3], 3:[]}

  - 邻接顶点

    - 无向图：由一条边连接起来的两个顶点，互为邻接顶点

      ```
        for i, j in edges:   
            graph[j].append(i)   
            graph[i].append(j)   
      ```

    - 有向图：u->v, u的邻接点是v，即指向的点为邻接点

      ```
        for i, j in edges:   
            graph[j].append(i)   
      ```

  - Adjacency Matrix（领接表）

    - 时间复杂度V^2

    

- 有环无环，单个多个

n个顶点，edges，无平行边

- 无环孤立
  - n == 1，len(edges)==0
  - n > 1 --> n = len(edges) + 1
- 有环孤立
  - 可以是多个环
  - n < len(edges) + 1
- 无环多个
  - n > len(edges) + 1
- 有环多个
  - n >=< len(edges) + 1

## 1.2 常见题型

**诀窍**
**用BFS时，append之后立刻visited = 1，以防重复出错**

### 1.2.1 无向图

- 判断两点之间是否相连（遍历）
- 是否有环
  - DFS: visited(0,1)；parent法；核心：无环的时候，其访问过的节点有且只有一个，并且是其上一个节点
  - BFS: 同DFS
  - Union find: root1 == root2则有环
- 孤立个数
  - DFS
  - BFS
  - Union find: n(节点个数) - numb(连接的次数）
- Biconnectivity
  -  Is there a vertex whose removal disconnects the graph?
- 路径层数
- 路径和
- 最短路径
- 最小生成树

### 1.2.2 有向图

- 判断a点能否到达b点（遍历）
- 是否有环
  - DFS: visited(-1, 0, 1)；核心：遇到正在被访问的node(visited[i] == 0)，则有环
  - Topo sort: indegree / outdegree; 遍历完之后，有入度不为0的node，则有环
- 孤立个数
  - DFS / BFS
- 路径层数
- 路径和
- 最短路径
- 最长路径

## 1.3 时间空间复杂度

- DFS

- BFS

  时间空间都是 O(E+V)
  **空间**：

  - 建立visited，用V
  - 建立graph，用E
  - DFS：会有保存的栈，也就是考虑最大层数，最坏情况是有V层
  - BFS：会有保存的栈，也就是考虑最宽的层，最坏情况是E

  **时间**：

  - 建立visited，V
  - 建立graph，V
  - 遍历edges，E
  - DFS/BFS遍历图，V

- 并查集
- 拓扑



# 2 题目

## 2.1 图的基础

- 133.Clone Graph 



## 2.2 无向图

**判断孤立和分群**

- 323.Number of Connected Components in an Undirected Graph(并查集) 
- 547.Friend Circles(并查集)
- 1202.Smallest String With Swapy

**判断环**

- 261.Graph Valid Tree

**路径和-求层数**

- 无向图的最长距离.py



## 2.3 有向图

**判断孤立个数和分群**

- 841.Keys and Rooms 

**判断环**

- 207.Course Schedule
- 802.Find Eventual Safe States 

**路径和-求层数**

- 1376.Time Needed to Inform All Employees 
- 210.Course Schedule II 
- 399.Evaluate Division 
- 444.Sequence Reconstruction 
- 程序的依赖关系.py 
- 1376[ 通知所有员工所需的时间](https://leetcode-cn.com/problems/time-needed-to-inform-all-employees) 



## 2.4 网格搜索

- 200.Number of Islands 
- 733.Flood Fill 



## 2.5 笔记

- 无向图遍历-BFS.py
- 无向图遍历-DFS.py
- 无向图判断是否有环.py
- 有向图判断是否有环.py
- 拓扑排序.py
- 并查集.py

**未完成**

- 无向图的最长距离


图的建立与应用	565
深度优先搜索	17、397
回溯法	526、401、36、37、51、52、77、39、216、40、46、47、31、556、60、491、78、90、79、93、332
回溯法与表达式	241、282、679
回溯法与括号	22、301
回溯法与贪心	488
广度优先搜索	133、200、695、463、542、130、417、529、127、126、433、675
并查集	547、684、685
拓扑排序	399、207、210
有限状态自动机	65、468



# 代码总结

## 3.1 无向图

### 3.1.1 遍历

#### 3.1.1.1 DepthFirstPath

* 深度优先
  * preorder
  * postorder

**In python**

```python
# 如果不是从0开始的node
from collections import defaultdict
pairs = [[1,2],[3,2]]
graph = defaultdict(list)
for i, j in pairs:
    graph[i].append(j)
graph
```



```python
class Graph:
    def DFS_Traversal(self, nums, pairs):
        def dfs(node):
            if visited[node] == 1:
                return 
            
            preorder.append(node)  # 前序遍历
            visited[node] = 1
            for out in adjacent[node]:
                dfs(out)

            postorder.append(node)  # 后序遍历
            return 

        # corner case
        if nums == 0 or pairs == []:
            return
        
        # make visited list and adjacent list
        visited = [0] * nums
        adjacent = [[] for _ in range(nums)]
        for i, j in pairs:
            adjacent[i].append(j)
            adjacent[j].append(i)

        # traversal the graph
        preorder = []
        postorder = []
        for i in range(nums):
            if visited[i] == 0:
                dfs(i)
        
        print(preorder)
        print(postorder)
        return 

x = Graph()
x.DFS_Traversal(5, [[0,1], [0,2], [0,3], [1,4]])

```



**In java**

```java
import java.util.List;
import java.util.ArrayList;

class Graph {
    int[] visited;
    List<List<Integer>> adjacent;
    ArrayList<Integer> postorder = new ArrayList<Integer>();
    ArrayList<Integer> preorder = new ArrayList<Integer>();

    public void DFStraversal(int nums, int[][] pairs) {
        if (nums == 0 || pairs.length == 0) return;

        visited = new int[nums];
        adjacent = new ArrayList<List<Integer>>();
        for (int i = 0; i < nums; i++) {
            adjacent.add(new ArrayList<Integer>());
        }

        for (int[] each: pairs) {
            adjacent.get(each[0]).add(each[1]);
            adjacent.get(each[1]).add(each[0]);
        }

        for (int i = 0; i< nums; i ++) {
            if (visited[i] == 0) {
                dfs(i);
            }
        }
        System.out.println(preorder);
        System.out.println(postorder);
        return;

    }

    /** traversal the graph*/
    private void dfs(int node) {
        if (visited[node] == 1) return;

        visited[node] = 1;
        preorder.add(node);
        for (int out: adjacent.get(node)) {
            dfs(out);
        }
        postorder.add(node);
        return;
    }

    public static void main(String[] args) {
        int nums = 5;
        int[][] pairs = {{0,1}, {0,2}, {0,3}, {1,4}};
        Graph graph = new Graph();
        graph.DFStraversal(nums, pairs);

    }
}

```

#### 3.1.1.2 BreadthFirstSearch

* 广度优先

**In python**

```python
from collections import deque

class Graph:
    def BFS_Traversal(self, nums, pairs):
        # corner case
        if nums == 0 or pairs == []:
            return
        
        visited = [0] * nums
        adjacent = [[] for _ in range(nums)]
        for i, j in pairs:
            adjacent[i].append(j)
            adjacent[j].append(i)

        order = []
        queue = deque()
        for i in range(nums):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1  # 切记，append之后立刻visited变成1

                while queue:
                    node = queue.popleft()
                    order.append(node)

                    for out in adjacent[node]:
                        if visited[out] == 0:
                            queue.append(out)
                            visited[out] = 1
        print(order)
        return 

x = Graph()
x.BFS_Traversal(5, [[0,1], [0,2], [0,3], [1,4]])

```



**In java**

```Java
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Graph {
    int[] visited;
    List<List<Integer>> adjacent;
    ArrayList<Integer> order = new ArrayList<Integer>();

    public void BFStraversal(int nums, int[][] pairs) {
        if (nums == 0 || pairs.length == 0) return;

        visited = new int[nums];
        adjacent = new ArrayList<List<Integer>>();
        for (int i = 0; i < nums; i++) {
            adjacent.add(new ArrayList<Integer>());
        }

        for (int[] each: pairs) {
            adjacent.get(each[0]).add(each[1]);
            adjacent.get(each[1]).add(each[0]);
        }

        Queue<Integer> queue = new LinkedList<Integer>();
        for (int i = 0; i < nums; i++) {
            if (visited[i] == 0) {
                queue.offer(i);
                visited[i] = 1;

                while (!queue.isEmpty()) {
                    int node = queue.poll();
                    order.add(node);
                    System.out.println(node);

                    for (int out : adjacent.get(node)) {
                        if (visited[out] == 0) {
                            queue.offer(out);
                            visited[out] = 1;
                        }
                    }
                }
            }
        }
        System.out.println(order);
        return;
    }

    public static void main(String[] args) {
        int nums = 5;
        int[][] pairs = {{0,1}, {0,2}, {0,3}, {1,4}};
        Graph graph = new Graph();
        graph.BFStraversal(nums, pairs);
    }
}
```



### 3.1.2 判断环

#### 3.1.2.1 DFS的01，parent法则

* 用visited来记录是否已经被访问过（0，1法则）
* 同时记录该节点的parent node
* **无环：其访问过的节点有且只有一个，并且是其节点的上一个节点（parent_index)**



**In python**

```python
# True: 有环
# False: 没有环
# 无环：其访问过的节点有且只有一个，并且是其节点的上一个节点（parent_index)

class Graph:
    def findCircle(self, nums, pairs):
        if nums == 0 or pairs == [] or pairs == [[]]: 
            return False
        '''
        判断是否无圈且是一个component
        if n == 0:
            return False
  			# n=2, pairs = [] --> 多个component
        if n - 1 != len(edges):
            return True
        '''
        visited = [0] * nums
        graph = [[] for _ in range(nums)]
        
        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)
            
        def dfs(index, parent):
            visited[index] = 1
            
            for j in graph[index]:
                if visited[j] == 0:
                    if dfs(j, index) == True:
                        return True
                elif j != parent:
                    return True
            return False
            
        for i in range[nums]:
            if visited[i] == 0:
                if dfs(i, -1) == True:
                    return True
        return False
      
```



**In java**

```java
/** True: 有环*/
private Boolean dfs(int node, int parent) {
    visited[node] = 1;
    for (int out: adjacent.get(node)) {
        if (visited[out] == 0) {
            if (dfs(out, node) == true) {
                return true;
            }
        } else {
            if (out != parent) {
                return true;
            }
        }
    }
    return false;
}
```



#### 3.1.2.2 BFS的01，parent法则

**In python**

```python
# True: 有环
# False: 没有环

from collections import deque, defaultdict
class Graph:
    def findCircle(self, nums, pairs):
        if nums == None or pairs == None:
            return False
        
        visited = [0] * nums
        graph = defaultdict(set)
        queue = deque()
        
        for i, j in pairs:
            graph[i].add(j)
            graph[j].add(i)
            
        for i in range(nums):
            if visited[i] == 0:
                queue.append([i,-1])
            
            while queue:
                index, parent = queue.popleft()
                visited[index] = 1
                
                for out_index in graph[index]:
                    if visited[out_index] == 0:
                        queue.append([out_index, index])
                    elif out_index != parent:
                        return False
        return True
        
```



**In java**

```java

```



#### 3.1.2.3 Union Find

* Union find by rank and path compression
* if root1 == root2 则有环

**In python**

```python
# True: 有环
# False: 没有环

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        if len(edges) == 0:
            return n
        
        def find(i):
            if gT[i] == i:
                return i
            else:
                return find(gT[i])

        count = 0
        gT = [x for x in range(n)]
        rank = [1] * n
        for i, j in edges:
            root1 = find(i)
            root2 = find(j)

            if root1 == root2:
                return True
            else:
                if rank[i] >= rank[j]:
                    rank[i] += rank[j]
                    gT[root2] = root1
                else:
                    rank[j] += rank[i]
                    gT[root1] = root2
        return False
```



**In java**

```java
// union find 见岛屿个数处
```



### 3.1.3 孤立岛屿个数

* DFS 0 1 法则
* BFS 0 1 法则
* Union find

**In python**

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        if len(edges) == 0:
            return n
        
        def find(i):
            if gT[i] == i:
                return i
            else:
                return find(gT[i])

        count = 0
        gT = [x for x in range(n)]
        for i, j in edges:
            root1 = find(i)
            root2 = find(j)

            if root1 == root2:
                pass
            else:
                gT[root2] = root1
                count += 1
        return n - count
```



**In java**

```java
class Solution {
    private int[] gT;
    private int[] size;

    public int countComponents(int n, int[][] edges) {
        gT = new int[n];
        size = new int[n];
        int count = n;

        for (int i = 0; i < n; i += 1) {
            gT[i] = i;
            size[i] = 1;
        }

        for (int [] e : edges) {
            int root1 = find(e[0]);
            int root2 = find(e[1]);
            if (root1 == root2) continue;

            if (size[root1] >= size[root2]) {
                gT[root2] = root1;
                size[root1] += size[root2];
            } else {
                gT[root1] = root2;
                size[root2] += size[root1];
            }

            count -= 1;
        }

        for (int i = 0; i < n; i++) {
            if (gT[i] == i) {
                System.out.print(size[i]);
            }
        }

        return count;
    }

    private int find(int i) { 
        while (gT[i] != i) {
            gT[i] = gT[gT[i]];
            i = gT[i];
        }
        return i;
    }
}
```

### 3.1.4 路径类



#### 3.1.4.1 所有路径



#### 3.1.4.2 最短路径

？



#### 3.1.4.3 最小生成树(MST)

* Minimum Spanning Trees
* acyclic
* 只考虑the graph is connected, 如果有多个component，分别求最小生成树，然后合并在一起
* 如果不同边的权重可以相同，那么最小生成树就不是唯一性的了，当所有边的权重都各不相同时，就只有一个最小生成树

* 1584

![截屏2020-11-24 上午9.27.37](/Users/leah/Dropbox/Leetcode/CS61B/CS61B_Xu/notebook/graph/截屏2020-11-24 上午9.27.37.png)

* prim是从一点出发，每一点都是连在一起的
* kruskal是一块块来，最后都连在一起



##### Prim‘s Algorithm

**思路**

- 关键点在于每次都找两点之间的最短，把所有点连接起来就是最小生成树
- 把所有点以inf的起始放入
- 随意找一个起始点，起始权重是0
- 每一次pop最短的那个点
- 遍历其相邻点，改变path， 这里的path是指两点之间的最短权重
  - Dijkstra里面的path是source点到该点之间的最短权重
- 注意已经找到最短的点就不要再继续找了

```python
# 方法一，非heap
# 按点为基准，遍历点
def Prim_findMST(self, n, edges):
    adj = defaultdict(dict)
    for i, j, w in edges:
        adj[i][j] = w
        adj[j][i] = w
    
    count = 0
    res = {}
    dist = {node: float('inf') for node in range(n)}
    dist[0] = 0

    while dist:
        i, w = sorted(dist.items(), key = lambda x:x[1])[0]
        dist.pop(i)

        res[i] = w
        count += w

        for j in adj[i]:
            if j not in res:
                dist[j] = min(dist[j], adj[i][j])
    
    return count
  
# 方法二
# heap里面放边，遍历边
def findMST(self, n: int, edges: List[List[int]]):  # node: 0-start
    # adjancent list
    adj = defaultdict(dict)

    for i, j, w in edges:
        adj[i][j] = w
        adj[j][i] = w

    heap = [(0, 0)]  # path, node
    res = {}
    count = 0

    while heap:
        w, i = heappop(heap)

        if i not in res:
            count += w
            res[i] = w

        if len(res) == n:
            break

        for j in adj[i]:
            if j not in res:
                heappush(heap, (adj[i][j], j))

    return count

```



##### Kruskal's Algorithm

- insert all edges into PQ
- Repeat: Remove smallest weight edge. Add to MST if no cycle created
  - check cycle: Union(node1, node2)

```python
def kruskal(pair, n):
    def find(v):
        while groupTag[v] != v:
            groupTag[v] = groupTag[groupTag[v]]
            v = groupTag[v]
        return v
    
    def union(root1, root2):
        if rank[root1] < rank[root2]:
            root1, root2 = root2, root1
        rank[root1] += rank[root2]
        groupTag[root2] = root1
        
        return
    
    heap = [(w, i, j) for i, j, w in pair]
    heapify(heap)
    
    res = 0
    edgeTime = 0
    groupTag = {i:i for i in range(n)}
    rank = {i : 1 for i in range(n)}
    
    while edgeTime != n - 1:  # 前提是所有的点都在一个component上
        w, i, j = heappop(heap)
        root1 = find(i)
        root2 = find(j)
        if root1 != root2:
            union(root1, root2)
            res += w
            edgeTime += 1
    return res


```



## 3.2 有向图

### 3.2.1 遍历

* 构建连接表的时候
  * 无向图：由一条边连接起来的两个顶点，互为邻接顶点

    ```
      for i, j in edges:   
          graph[j].append(i)   
          graph[i].append(j)   
    ```

  * 有向图：u->v, u的邻接点是v，即指向的点为邻接点

    ```
      for i, j in edges:   
          graph[j].append(i)   
    ```

* DFS
* BFS

#### 3.2.1.1 Topological Sort

##### 广度优先

* **topological ordering is given by the reverse of that list(reverse postorder)**
  * `[2, 5, 6, 0, 3, 1, 4, 7]`
  * 把这些nodes都整理一下就是下面的图
  * 遍历方向都是朝着右边的 

![截屏2020-12-05 下午4.38.41](/Users/leah/Dropbox/Leetcode/CS61B/CS61B_Xu/notebook/graph/截屏2020-12-05 下午4.38.41.png)

##### 宽度优先





### 3.2.2 判断环

#### 3.2.2.1 DFS [-1,0,1]法则

* 遇到正在被访问的点，则说明有环



#### 3.2.2.2 拓扑



### 3.2.3 孤立岛屿个数

* 模版同无向图





### 3.2.4 路径类

#### 3.1.4.1 所有路径



#### 3.1.4.2 最短路径





#### 3.1.4.3 最小生成树

不能用Prim‘s Algorithm和Kruskal's Algorithm的原因：

1->2 8, 1->3 8, 2->3 4, 3->2 3   
有平行边的时候，且其它边都是相等的距离，那么不一定能得到最小生成树

