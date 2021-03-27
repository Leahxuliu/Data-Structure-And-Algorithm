'''
brout force
use backtracking to simulate game 
'''

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def check(start, end, player1, player2, flag):
            print(start, end, self.flag2)
            if self.flag2 == True:
                return True

            if (start, end, flag) in info:
                return info[(start, end, flag)]

            if start > end:
                return player1 > player2
            
            res = False
            if flag == 0:
                res1 = check(start + 1, end, player1 + piles[start], player2, 1)
                res2 = check(start, end - 1, player1 + piles[end], player2, 1)
                if res1 == True or res2 == True:
                    res = True
                    self.flag2 = True
                info[(start, end, flag)] = res
                
            else:
                res1 = check(start + 1, end, player1, player2 + piles[start], 0)
                res2 = check(start, end - 1, player1, player2 + piles[end], 0)
                if res1 == False or res2 == False:
                    res = True
                    self.flag2 = True
                info[(start, end, flag)] = res
            
            return res

        
        info = {}
        self.flag2 = False
        return check(0, len(piles) - 1, 0, 0, 0)