#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
# find操作是为每一个节点找到它的最远祖先，如果节点对应的数值为初始的index的话，证明其依然为isolate，
# 如果不是的话，存储的index为其祖先的index，这样就能find其最远祖先

    def find(self, index, groupTag):
        # isolate
        if group[index] == index:
            return index
        # group
        else:
            return self.find(groupTag[index], groupTag)

# Union操作，进来的这两个节点是联通的，union函数是将这两个节点合并成一个组。通过调用find操作，对两个节点找到其祖先
# 然后如果祖先相同的话，证明这两个节点已经再一个组里，跳过；如果不是的话，将第二个节点的祖先设置为第一个节点
    def union(self, i, j, groupTag):
        root1 = self.find(i, groupTag)
        root2 = self.find(j, groupTag)
        # already unioned
        if root1 == root2:
            return
        else:
            groupTag[root2] = root1  # 连接新点
    
    def groups(n, pairs):
        # 初始化，每一个点都设置为单独的一个组，标记为index
        groupTag = [i for i in range(n)]  # 即每个i都用其index = i进行标记
        
        for i, j in pairs:
            self.union(i, j, groupTag)
        
        #针对Union-find的缺陷进行修正，详细见上文
        for i in range(len(groupTag)):
            groupTag[i] = self.find(groupTag[i], groupTag)

x = Solution()
x.find(5, [[0,1], [0,2], [0,3], [1,4]])