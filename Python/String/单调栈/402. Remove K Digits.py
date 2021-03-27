# 贪心 + 单调递增栈
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n < k:
            return 0
        
        stack = [-1]
        count = 0
        for i in range(n):
            if i == 0:
                stack.append(num[i])
            
            else:
                while int(num[i]) < int(stack[-1]) and count < k:
                    stack.pop()
                    count += 1
                stack.append(num[i])

        while count < k:
            stack.pop()
            count += 1

        start = 0
        for i in range(len(stack)):
            if int(stack[i]) > 0:
                start = i
                break
        if start == 0:
            return "0"
        else:
            return "".join(stack[start:])


# 代码优化

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in num:
            while k and stack and int(i) < int(stack[-1]):
                stack.pop()
                k -= 1
            stack.append(i)

        while k > 0 and stack:
            k -= 1
            stack.pop()
        
        res = ''.join(stack).lstrip('0')
        return res if res != '' else '0'