'''
链表深copy，可能有环，也可能没有环
'''


'''
是否有重复数？
若无重复数，用一个visited来记录访问点的值  行不通！因为没法curr.next = cycle beginer


1. 判断是否有环
2. 若有环，找环交点，记录环交点
3. 构建新链表
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def copy_node(head):
    '''
    deep copy NodeList
    return new root
    '''

    # corner case
    if head == None:
        return None
    
    # visited = set()
    # new_head = Node(0)
    # curr = new_head

    # while head:
    #     if head in visited:
    #         curr.next = 
    #     visited.add(head)
    #     curr.next = Node(head.val)
    #     curr = curr.next 

    # check cycle
    s = head
    f = head
    meet = None 
    while s and f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            meet = s
            break
    
    s = head
    f = meet 
    while s != f and f:
        s = s.next
        f = f.next
    
    meet = f 

    # deep copy nodelist
    new_root = Node(0)
    curr = new_root
    new_meet = None

    while head:
        
        if meet:
            # first time meet 
            if head == meet and new_meet == None:
                curr.next = Node(head.val)
                curr = curr.next
                new_meet = curr
                head = head.next
            
            # second time
            elif head == meet and new_meet:
                curr.next = new_meet
                break

        curr.next = Node(head.val)
        curr = curr.next
        head = head.next
    
    return new_root.next


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

one.next = two
two.next = three
three.next = four
four.next = two

new = copy_node(one)

for i in range(6):
    print(one.val, new.val)
    one = one.next
    new = new.next

