'''
https://leetcode.com/discuss/interview-question/373202
'''

a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

def OptimalUtilization(a, b, target):
    a = sorted(a, key=lambda x: x[1])
    b = sorted(b, key=lambda x: x[1])

    
