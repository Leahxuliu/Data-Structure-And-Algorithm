# 回溯

class Solution:
    def countVowelStrings(self, n: int) -> int:
        def helper(start, word):
            if len(word) == n:
                #all_res.append(word[:])
                self.res += 1
                return
                
            for i in range(start, len(info)):
                #print(i)
                word.append(info[start])
                helper(i, word)
                word.pop()
                
            return
        
        info = ["a","e","i","o","u"]
        self.res = 0
        #all_res = []
        
        helper(0, [])
        return self.res
        

# 隔板法
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 5 - 1, 4)
