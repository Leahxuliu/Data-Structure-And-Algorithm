# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
'''
非图的算法题

outdegree:0 + indegree:n-1 --> celebrity

asking:
找celebrity候选人
1. 先假设0是celebrity，探测是否认识其他人（只遍历本序号之后的人）
    若认识i，下一个celebrity就是i
    都不认识，0就有可能是celebrity
    
2. 验证该候选人是否是celebrity
    a.是否都不认识其他的人
    b.验证大家都认识celebrity

'''


class Solution:
    def findCelebrity(self, n: int) -> int:
        if n == 0:
            return -1
        
        # 找到出度为0的点
        # 遍历方式想成（相当于快慢双指针）
        celeb = 0
        for i in range(n):
            if knows(celeb, i):
                celeb = i 
        
        # 判断该候选人是不是真的是celeb
        for i in range(n):
            if i != celeb:
                # celeb不认识任何人
                if knows(celeb, i):
                    return -1
                # 所有人认识celeb
                if knows(i, celeb) == False:
                    return -1
       
        return celeb