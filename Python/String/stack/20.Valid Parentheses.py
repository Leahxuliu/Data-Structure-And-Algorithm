'''
stack
左括号append
右括号pop
看是否是一对
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        data = {')':'(', ']':'[', '}':'{'}

        stack = []
        for i in s:
            if i in data:
                if stack and stack[-1] == data[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if stack == [] else False  # 勿忘

