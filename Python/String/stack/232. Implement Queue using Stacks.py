'''
输入栈 + 输出栈模拟queue
pop和peak从输出栈里出，所以输出栈是空的时候，把输入栈里的东西都倒到输出栈里

'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lstIn = []
        self.lstOut = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.lstIn.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.lstOut == []:
            while self.lstIn:
                self.lstOut.append(self.lstIn.pop())
        return self.lstOut.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.lstOut == []:
            while self.lstIn:
                self.lstOut.append(self.lstIn.pop())
        return self.lstOut[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.lstOut == [] and self.lstIn == []