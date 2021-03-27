'''
       whitespace  character  sign  integer
start     start       end      sign   integer
sign       end       end      end    integer
integer    end    end      end    integer
end

还有小数点等符号 3.14
i.isalpha() 是不能判断的

"+-12" --> 0
"00000-42a1234" --> 0
"   +0 123"  --> 0

把sign与integer分开保存很容易出错，所以合并在一起，用string的形式保存res
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        res = ''

        for i in s:
            if i == ' ' and len(res) == 0:  # 易错
                continue
            elif i.isdigit():
                res += i
            elif i == '+' or i == '-':
                if len(res) != 0:
                    break
                else:
                    res += i
            else:
                break

        if res == '' or res == '+' or res == '-':
            return 0
        if res[0] == '+':
            res = int(res[1:])
            return res if res < 2147483647 else 2147483647
        if res[0] == '-':
            res = int(res[1:]) * (-1)
            return res if res > -2147483648 else -2147483648
        return int(res) if int(res) < 2147483647 else 2147483647


# 状态机
'''
       whitespace  character  sign  integer
start     start       end      sign   integer
sign       end       end      end    integer
integer    end    end      end    integer
end

还有小数点等符号 3.14
i.isalpha() 是不能判断的

"+-12" --> 0
"00000-42a1234" --> 0
"   +0 123"  --> 0

把sign与integer分开保存很容易出错，所以合并在一起，用string的形式保存res
'''

from collections import defaultdict
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        atoi = defaultdict(dict)
        atoi['start']['space'] = 'start'
        atoi['start']['char'] = 'end'
        atoi['start']['sign'] = 'sign'
        atoi['start']['int'] = 'int'
        atoi['sign']['space'] = 'end'
        atoi['sign']['char'] = 'end'
        atoi['sign']['sign'] = 'end'
        atoi['sign']['int'] = 'int'
        atoi['int']['space'] = 'end'
        atoi['int']['char'] = 'end'
        atoi['int']['sign'] = 'end'
        atoi['int']['int'] = 'int'
        # print(atoi)

        state = 'start'
        res = 0
        flag = 1
        for i in s:
            if state == 'end':
                break

            if i.isspace():
                state = atoi[state]['space']
            elif i.isdigit():
                state = atoi[state]['int']
                if state != 'end':
                    res = res * 10 + int(i)
                    res = min(INT_MAX, res) if flag == 1 else min(-INT_MIN, res)
            elif i == '+' or i == '-':
                state = atoi[state]['sign']
                if state != 'end' and i == '-':
                    flag = -1
            else:
                state = 'end'

        return flag * res
                    
   
             
# 正则                    
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        pattern = re.compile(r'\s*[+\-]?\d*')
        res = re.search(pattern, s).group()

        res = res.lstrip()  # 清空左边的空格
        if res == '' or res == '+' or res == '-':
            return 0
        
        if res[0] == '+':
            res = int(res[1:])
            return res if res < INT_MAX else INT_MAX
        if res[0] == '-':
            res = -1 * int(res[1:])
            return res if res > INT_MIN else INT_MIN

        res = int(res)
        return res if res < INT_MAX else INT_MAX

        
             
        
    '''
把每一个条件写成一个def
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0
        
        # ignore the leading whitespace 
        def remove_whitespace(s):
            start = 0
            for i in range(len(s)):
                if s[i] != ' ':
                    start = i
                    break
            return start

        # check if the number is negative or positive
        def check(start):
            if s[start] == '-':
                return -1, start + 1
            elif s[start] == '+':
                return 1, start + 1
            return 1, start

        # string to integer
        def change(start):
            res = ''
            for i in range(start, len(s)):
                if s[i].isdigit() == False:
                    break
                res += s[i]
            return int(res) if res != '' else 0

        start = remove_whitespace(s)
        flag, start = check(start)
        res = change(start)

        res = flag * res
        if res < -1 * 2 ** 31:
            return -1 * 2 ** 31
        elif res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return res

        