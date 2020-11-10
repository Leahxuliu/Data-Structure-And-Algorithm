class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        info = {}

        for i, j in zip(ages, scores):
            if i in info:
                info[i].append(j)
            else:
                info[i] = [j]

        sortedInfo = sorted(info.items(), key = lambda x:x[0])

        newScore = []
        for a, s in sortedInfo:
            if len(s) == 1:
                newScore.append(s[0])
            else:
                s.sort()
                newScore += s
        dp = newScore[:]

        for i in range(1, len(ages)):
            for j in range(i):
                if newScore[j] <= newScore[i]:
                    dp[i] = max(dp[j] + newScore[i], dp[i])
        return max(dp)