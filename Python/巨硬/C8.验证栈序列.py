'''
946
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed == [] and popped == []:
            return True
        if pushed == [] or popped == []:
            return False
        
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)

            while j < len(popped) and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return True if j == len(popped) else False 

