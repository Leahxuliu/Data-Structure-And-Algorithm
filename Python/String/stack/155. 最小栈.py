# 建立两个list，一个用来保存val，一个用来保存minVal
# 用一个stack保存最小值
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.lst.append(val)
        if self.min_stack and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.lst.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()