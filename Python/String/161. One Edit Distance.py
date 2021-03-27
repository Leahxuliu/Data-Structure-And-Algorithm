'''
two pointers
i, j pointer start at s, t
use a flag to store used step or not
'''

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # corner case
        if s == '' and t == '':
            return False
        if s == t:
            return False
        if abs(len(s) - len(t)) > 1:
            return False

        i = 0
        j = 0
        used = False

        # replace
        if len(s) == len(t):
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    if used:
                        return False
                    used = True
                i += 1
                j += 1
        
        # insert
        elif len(s) + 1 == len(t):
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    if used:
                        return False
                    if j + 1 < len(t) and s[i] == t[j + 1]:
                        i += 1
                        j += 2
                    else:
                        i += 1
                        j += 1
                    used = True
                else:
                    i += 1
                    j += 1
        
        # delet
        else:
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    if used:
                        return False
                    if i + 1 < len(s) and s[i + 1] == t[j]:
                        i += 2
                        j += 1
                    else:
                        i += 1
                        j += 1
                    used = True
                else:
                    i += 1
                    j += 1

        if (i != len(s) or j != len(t)) and used == True:
            return False
        return True

'''
key:
find the diff, the check after diff, s==t or not
'''

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if abs(len(s) - len(t)) > 1:
            return False

        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return s[i + 1:] == t[j + 1:] or s[i:] == t[j + 1:] or s[i + 1:] == t[j:]
            i += 1
            j += 1

        return True