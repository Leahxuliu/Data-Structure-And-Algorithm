'''
394. 字符串解码
字符串(A2B3)2 = A4B6
'''

class Solution:
    def decodeString(self, s: str) -> str:
        if s == "":
            return ""
        
        stack = []
        count = 0

        for i in s:
            if i == ']':
                temp = ''
                while stack[-1].isdigit() == False:
                    temp = stack.pop() + temp
                temp = int(stack.pop()) * temp
                stack.append(temp)
            
            elif i == '[':
                stack.append(str(count))
                count = 0
            elif i.isdigit():
                count = count * 10 + int(i)
            else:
                stack.append(i)
        res = ''
        while stack:
            res = stack.pop() + res
        
        return res