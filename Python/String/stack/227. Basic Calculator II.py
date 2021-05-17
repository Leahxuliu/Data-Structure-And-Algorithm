'''
* stack
* 用flag来保存上一个符号
* 先把数存入stack，遇到符号，pop stack top数，与flag进行计算，也就是说这一次遇到option其实是对上一个option进行处理
* stack里面放需要进行加减的运算，乘除运算要先算出结果再放入stack
* 在s尾部加入一个“+”用来处理最后一个数


就算* / 要先算，也可以把前一个数先放入stack，
因为* / 前面就一个数，pop一下就可以

224不能像227这样
是因为（）里面可以有好多数
'''

class Solution:
    def calculate(self, s: str) -> int:
        s += '+'  # 用来处理最后一个数

        stack = []
        n = len(s)
        num = 0
        flag = '+'

        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            
            elif s[i] in '+-*/':
                if flag == '+':
                    stack.append(num)
                elif flag == '-':
                    stack.append(-1 * num)
                elif flag == '*':
                    pre = stack.pop()
                    stack.append(pre * num)
                elif flag == '/':
                    pre = stack.pop()
                    stack.append(int(pre / num))   #   -3 // 2 = -2；而题目需要等于-1
                num = 0
                flag = s[i]

        return sum(stack)
