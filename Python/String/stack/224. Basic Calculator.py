class Solution:
    def calculate(self, s: str) -> int:
        s += '+'

        flag = 1
        stack = []
        num = 0
        res = 0

        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == '+' or i == '-':
                res += flag * num
                num = 0
                flag = 1 if i == '+' else - 1
            elif i == '(':
                # 把括号前的res和flag先寄存在stack里
                stack.append(res)
                stack.append(flag)
                # 接下来要开始计算括号里的，所以res要归0
                res = 0
                flag = 1
            elif i == ')':
                # 先计算括号里面的
                res += flag * num
                num = 0
                flag = 1
                # 括号前的符号 * 现在括号内的res，然后括号前的res + 现在的res
                res = stack.pop() * res + stack.pop()
        # 最终stack里面是空的
        return res


