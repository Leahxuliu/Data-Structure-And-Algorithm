# -*- coding: utf-8 -*-
# @Time    : 2/27/2020  
# @Author  : XU Liu
# @FileName: constructTree.py

# define Node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# construct a Tree using deque and BFS
from collections import deque
def constructTree(nodeList):
    new_node = []  # 把list里面的数变成Node
    for elem in nodeList:
        if elem:
            new_node.append(TreeNode(elem))
        else:
            new_node.append(None)
    
    queue = deque()
    queue.append(new_node[0])  # 相当于一个容器，一进一出

    resHead = queue[0]  # 保存root，这里的root是具有tree属性的，也就是保存了整个tree
    i = 1

    while i <= len(new_node) - 1:   # bfs method building (通过bfs的方法，把这些node串联起来)
        head = queue.popleft()  

        head.left = new_node[i]  # build left(i=1,node1的右边是node2)
        if head.left:
            queue.append(head.left)

        if i + 1 == len(new_node):  # 特例：比如[1,2,3,4,None,5]，最右边的最后一个数没有right的时候，这里需要break
            break

        head.right = new_node[i + 1]  # build right
        if head.right:
            queue.append(head.right)

        i = i + 2
    
    return resHead


if __name__ == '__main__':
    root = constructTree([1,2,3,4,None,5])
    #p = constructTree([1,2,3])
    #q = constructTree([1,2,3])
    

    def bsf(root):
        if  root == None:
            return 
        else:
            queue = deque()
            queue.append(root)  # 输入的是root的值，但是root带有属性，也就是tree
            while queue:
                node = queue.popleft()
                print(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

    
    bsf(root)

    