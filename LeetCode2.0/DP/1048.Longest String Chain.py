'''
Method - DP
DP[i]: the Longest String Chain in words[0: i + 1]

Steps:
    0. sort words by len(words)
    1. build a dp list, the size of list is the number of words
    2. i: 1-n; j:0-i
       dp[i] = max(dp[i], dp[j] + 1), words[i] is from words[i - 1]
       dp[0] = 1

'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        
        if n == 0:
            return 0
        
        def helper(w1, w2):
            if len(w2) - 1 != len(w1):
                return False
            
            for i in range(len(w2)):
                if w1 == w2[:i] + w2[i+1:]:
                    return True
            return False
        
        new_words = sorted(words, key = lambda x:len(x))
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if helper(new_words[j], new_words[i]) == True:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        print(dp)
        return max(dp)