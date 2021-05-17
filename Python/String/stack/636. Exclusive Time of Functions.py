'''
用stack来储存ID
start的时候把ID和start time放入stack
end的时候把ID pop出stack, 同时把上一个ID的start time改成这次end time + 1
'''

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if logs == []:
            return [0] * n

        stack = []
        res = [0] * n
        for each in logs:
            each = each.split(':')
            each = [int(each[0]), each[1], int(each[2])]
            if each[1] == 'start':
                if stack:
                    ID, time = stack[-1][0], stack[-1][1]
                    res[ID] += each[2] - time
                stack.append([each[0], each[2]])
            
            else:
                ID, time = stack.pop()
                res[ID] += each[2] - time + 1
                if stack:
                    stack[-1][1] = each[2] + 1
        return res