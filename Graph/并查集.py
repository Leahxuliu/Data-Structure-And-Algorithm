#!/usr/bin/python
# -*- coding: utf-8 -*-

# union-find method
# 用并查集判断有几类
# 并查集的核心：归类
# 比如 pairs [[0,1],[1,2],[3,4]]
# 0 -> 1 -> 2 
# 3 -> 4
# groupTag = [0,0,0,0,0] -> [0,0,0,3,3]

class Solution:

    def groups(self, n, pairs):
        # 初始化，每一个点都设置为单独的一个组，标记为index
        groupTag = [i for i in range(n)]  # GT = [0,1,2,3,4]
        
        # Union操作，进来的这两个节点是联通的，union函数是将这两个节点合并成一个组。通过调用find操作，对两个节点找到其祖先
        # 然后如果祖先相同的话，证明这两个节点已经再一个组里，跳过；如果不是的话，将第二个节点的祖先设置为第一个节点
        connect = 0
        for i, j in pairs:
            root1 = self.find(i, groupTag)
            root2 = self.find(j, groupTag)
            # already unioned
            if root1 == root2:
                pass
            else:
                groupTag[root2] = root1  # 连接新点
                connect += 1  # 扩展次数，不包括环的 比如 0-1-2， 三个数，两次扩展
        return n - connect  # 群的个数 = n - 扩展次数； 因为当所有node都相连（不包含环）需要n-1个扩展线，也就是connct的值，没增加一个群，也就是减少一个connect
        

    # find操作是为每一个节点找到它的最远祖先，如果节点对应的数值为初始的index的话，证明其依然为isolate，
    # 如果不是的话，存储的index为其祖先的index，这样就能find其最远祖先
    def find(self, index, groupTag):
        # isolate
        if groupTag[index] == index:
            return index
        else:
            return self.find(groupTag[index], groupTag)


x = Solution()
x.groups(5, [[0,1],[1,2],[3,4]])