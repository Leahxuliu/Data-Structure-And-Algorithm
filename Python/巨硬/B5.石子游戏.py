'''
877
'''

'''
1. 用相对分数，play1加分数，play减分数
2. 不是比较左右，取最大，而是比较取左之后，别人取了有的情况
brout force
backtracking to simulation stone game
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def play_game(start, end):
            '''
            先取的人尽可能最大
            '''
            if (start, end) in memo:
                return memo[(start, end)]

            if start == end:
                return piles[start]
            
            choose_left = piles[start] - play_game(start + 1, end)
            choose_right = piles[end] - play_game(start, end - 1)
            
            res = max(choose_left, choose_right)
            memo[(start, end)] = res
            return res
        
        memo = {}
        return play_game(0, len(piles) - 1) > 0


'''
dp

状态 dp[i][j] 定义：区间 piles[i..j] 内先手可以获得的相对分数；
状态转移方程：dp[i][j] = max(nums[i] - dp[i + 1, j] , nums[j] - dp[i, j - 1]) 。

类似最长回文子序列？
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = piles[i]
                else:
                    dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        
        return dp[0][-1] > 00



'''
错误
brout force
backtracking to simulation stone game
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def play_game(start, end, play1, play2, flag):
            if self.res:
                return 
            if start > end:
                if play1 > play2:
                    self.res = True
                return 
            
            # alex
            if flag == 1:
                play_game(start + 1, end, play1 + piles[start], play2, 2)
                play_game(start, end - 1, play1 + piles[end], play2, 2)
            else:
                play_game(start + 1, end, play1, play2 + piles[start], 1)
                play_game(start, end - 1, play1, play2 + piles[end], 1)
            return 
        
        self.res = False
        play_game(0, len(piles) - 1, 0, 0, 1)
        return self.res