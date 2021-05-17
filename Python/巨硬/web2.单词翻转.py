'''
151

Input: s = "the sky is blue"
Output: "blue is sky the"
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "":
            return ""
        
        res = []
        word = ''
        for i in range(len(s)):
            if s[i] == " ":
                if word != "":
                    res.append(word)
                    word = ""
            else:
                word += s[i]
        if word != "":
            res.append(word)

        reverse = ""
        while res:
            reverse += res.pop() + " "
        
        reverse = reverse.rstrip(" ")
        return reverse



class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "":
            return ""
        
        s = s[::-1]
        s = s.split()
        
        new = []
        for word in s:
            new.append(word[::-1])

        return ' '.join(new) 



'''
186

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

先 整体 翻转，再挨个单词翻转
'''

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s == []:
            return []
        if len(s) == 1:
            return s 
        
        def reverse(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

            return 
        
        reverse(0, len(s) - 1)

        s.append(" ")
        left = 0
        for i in range(len(s)):
            if s[i] == " ":
                reverse(left, i - 1)
                left = i + 1
        s.pop()
        return 