# 用一个stack来储存最小值， 当前lst长度时的最小值
# 要么是新加入的val，要么是原本就是在端顶的值再加一遍

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        self.min_lst = []


    def push(self, val: int) -> None:
        self.lst.append(val)
        if self.min_lst and val > self.min_lst[-1]:
            self.min_lst.append(self.min_lst[-1])
        else:
            self.min_lst.append(val)
        return 

    def pop(self) -> None:
        self.lst.pop()
        self.min_lst.pop()
        return 

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.min_lst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()