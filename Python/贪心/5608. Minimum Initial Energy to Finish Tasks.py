class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        if len(tasks) == 1:
            return tasks[0][1]
        
        t = sorted(tasks, key = lambda x:x[0] - x[1])
        start = 0
        use = 0
        for i in range(len(t)):
            start = max(use + t[i][1], start)
            use += t[i][0]
        return start