'''
dict + two pointers

1. use dict to save the position of char
2. fast and slow pointers
    if s == f, cut

  a b a b c b a c a    d e f e g d e     h i j h k l i j
  s s s s s s s s s    s s s s s s s
  f               f              f f



'''

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        info = {}
        for i, each_s in enumerate(S):
            info[each_s] = i
        
        s = 0
        f = 0
        res = []
        for i, each_s in enumerate(S):
            max_p = info[each_s]
            f = max(max_p, f)
            if f == i:
                res.append(f - s + 1)
                s = i + 1
            
        return res

