'''
Method - Greedy
Steps:
    1. traverse pushed, put i into stack
    2. if stack[-1] == popped[0], pop stack

Time complexity: O(N)
Space: O(N)

'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed == []:
            return True
        if pushed == popped:
            return True
        
        j = 0
        stack = []
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return stack == []
        