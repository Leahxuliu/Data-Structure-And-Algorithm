def checkbalance(root):
    if root == None:
        return True
    
    def check(root, depth):
        if root == None:
            return 
        
        depth += 1
        l = check(root.left, depth)
        r = check(root.right, depth)

        return True if abs(l - r) <= 1 else False 
    
    return check(root, 0)