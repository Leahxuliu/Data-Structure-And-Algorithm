'''
先将所有字符翻转，再翻转每个单词，即得到想要的结果。
'''

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # corner case
        if s == []:
            return 
        if len(s) == 1:
            return 
        
        # reverse all char in the list
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        # add " " into list
        s.append(" ")

        # reverse each word
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                end = i - 1
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                start = i + 1
        
        s.pop()
        return