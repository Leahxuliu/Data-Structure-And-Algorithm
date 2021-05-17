'''
不能只用stack，左括号append，右括号pop
原因：()(() 不连续

改进：
1. 用stack，左括号append，右括号pop，同时记录index
2. 对这些index进行排序
3. 最长连续子串个数就是答案

因为右排序，所以时间复杂度是NlogN
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        
        stack = []
        pair = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    # 储存左括号的index
                    pair.append(stack.pop())
                    # 右括号的index
                    pair.append(i)
        
        if pair == []:
            return 0

        pair.sort()
        res = 0
        left = 0
        for right in range(1, len(pair)):
            if pair[right] == pair[right - 1] + 1:
                continue
            
            res = max(res, right - left)
            left = right
        return max(res, right - left + 1)
