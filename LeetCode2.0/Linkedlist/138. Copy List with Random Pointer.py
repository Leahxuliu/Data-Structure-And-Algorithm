# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/26

'''
Method
A. DFS + Dict
Steps:
    1. 用dfs helper函数从头开始遍历整个图,同时保存新的node到dict，key是原本的node，value是新建的node
    2. 如果已经有了当前节点的一个拷贝，return visitedHash[head]
    3. 如果还没拷贝过当前节点，创造一个新的节点，并把该节点放到已访问字典中,并
        node.next = helper(node.next);
        node.random = helper(node.random);
time complex: O(n)
space complex: O(n)

B. iterative + Dict
1. 遍历点，保存到dict
2. 新node.next和random都要用dict里已保存的node获得
time complex: O(n)
space complex: O(n)

C. iterative
time complex: O(n)
space complex: O(1)


'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# DFS + Dict
class Solution:        
    def copyRandomList(self, head):
        if head == None:
            return None

        def helper(head):
            if head == None:
                return None
            if head in newList:
                return newList[head]

            node = Node(head.val, None, None)
            newList[head] = node

            node.next = helper(head.next)
            node.random = helper(head.random)
            return node

        newList = {}
        helper(head)
        return newList[head]

# B 最好理解
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return 
        
        def getCloneNone(node):
            if node == None:
                return None

            if node not in info:
                info[node] = Node(node.val, None, None)
                return info[node]
            else:
                return info[node]

        info = {}
        curr = head
        while curr:
            if curr not in info:
                info[curr] = Node(curr.val, None, None)
            
            node = info[curr]
            node.next = getCloneNone(curr.next)
            node.random = getCloneNone(curr.random)

            curr = curr.next
        
        return info[head]


# C 不太理解
class Solution:
    def copyRandomList(self, head):
        if head == None:
            return None

        curr = head
        while curr:
            new_node = Node(curr.val, None,None)
            next_head = curr.next
            curr.next = new_node
            curr = next_head
            new_node.next = curr

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        #关键是：1.备份新头 2.判断老头退出条件
        new_head = new_node = head.next
        while head.next:
            head.next = head.next.next
            head = head.next
            if head == None:
                new_node.next = None
                break
            new_node.next = head.next
            new_node = new_node.next

        return new_head