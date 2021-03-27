'''
two pointer

1. traversal the s and t with pointers i and j
2. use a dictionary to store, key is s[i], value is t[j]

if b -> b, d -> b is also false x

"badc"
"baba"


'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        info = {}

        i = 0
        j = 0
        used = set()
        while i < len(s):
            if s[i] in info and info[s[i]] != t[j]:
                return False
            if s[i] not in info and t[j] in used:
                return False
            info[s[i]] = t[j]
            used.add(t[j])
            
            i += 1
            j += 1
        return True