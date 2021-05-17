class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def check(A, B):
            '''return true if overlap
            Args:
                A(list): [x1, x2] or [y1, y2] from rec1
                B(list): [x1, x2] or [y1, y2] from rec2
            Return:
                boolean
            '''
            a1, a2 = A 
            b1, b2 = B 
            # 一条线一个点不能叫做overlap
            if a1 == a2 or b1 == b2:
                return False

            return True if a1 < b2 and a2 > b1 else False
        
        if check([rec1[0], rec1[2]], [rec2[0], rec2[2]]) and check([rec1[1], rec1[3]], [rec2[1], rec2[3]]):
            return True 
        else:
            return False