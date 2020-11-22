class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if (len(people)) <= 1:
            return people

        res = []
        sortPeople = sorted(people, key = lambda x:(-x[0], x[1]))

        for i, j in sortPeople:
            if j >= len(res):
                res.append([i, j])
            else:
                res.insert(j, [i, j])
        return res