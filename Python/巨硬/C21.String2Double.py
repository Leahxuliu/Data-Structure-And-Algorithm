'''
8. String to Integer (atoi)

条件：
ignore 开头的空格
最初的 + or -表示正负
遇到non-digit就终止
变成int
超过32-bit 就取最小或最大值

'''
'''
把每一个条件写成一个def
'''

'''
String2Double
'''

class Solution:
    def myAtoi(self, s):
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
            if start > len(s):
                return 1, start

            if s[start] == '-':
                return -1, start + 1
            elif s[start] == '+':
                return 1, start + 1
            return 1, start

        # string to integer
        def change(start):
            if start > len(s):
                return 0, start

            end = start
            for i in range(start, len(s)):
                if s[i].isdigit() == False:
                    end = i
                    break
                res.append(s[i])
            return end 

        start = remove_whitespace(s)
        flag, start = check(start)

        res = []
        start = change(start)
        if start < len(s) and s[start] == '.':
            res.append('.')
            start = change(start + 1)

        return float(''.join(res)) * flag if res != [] else 0

        

a = Solution()
res = a.myAtoi("a-4193.1 with words")
print(res)