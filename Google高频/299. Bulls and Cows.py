
# time: O(n*n)
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # corner case
        if secret == '':
            return guess
        if guess == '':
            return ''

        secret_list = list(secret)
        guess_list = list(guess)

        # count bulls, A
        bulls = 0
        #for i in range(len(secret_list)):  # pop之后，长度发生变化
        i = 0
        while i < len(secret_list):
            if secret_list[i] == guess_list[i]:
                bulls += 1
                secret_list.pop(i)
                guess_list.pop(i)
            else:  # 特别易错
                i += 1

        # count cows, B
        cows = 0
        for j in guess_list:
            if j in secret_list:
                cows += 1
                secret_list.remove(j)
        return '%dA%dB' % (bulls, cows)

# 错误
from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if secret == '':
            return guess
        if guess == '':
            return ''
        
        # put the secret into dictionary
        info_secret = defaultdict(list)
        for i, s in enumerate(secret):
            info_secret[s].append(i)
        
        bulls = 0
        cows = 0
        for j, g in enumerate(guess):
            if g in info_secret:
                if j in info_secret[g]:
                    bulls += 1
                else:
                    cows += 1
        
        return '%dA%dB' % (bulls, cows)

# 订正
# time: O(n)
from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # corner case
        if secret == '':
            return guess
        if guess == '':
            return ''

        dict_secret = defaultdict(int)
        dict_guess = defaultdict(int)
        bulls = 0
        cows = 0


        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                dict_secret[secret[i]] += 1
                dict_guess[guess[i]] += 1
        
        for k in dict_guess.keys():
            if k in dict_secret:
                cows += min(dict_secret[k], dict_guess[k])  # 关键
        
        return '%dA%dB' % (bulls, cows)