'''
给定一个interval A和一组intervals,然后判断这组intervals里面是否存在一个并集是这个A的超集
'''

'''
[[2, 4], [5, 6],[3,5]]
[1, 4]
一组intervals合并之后，并没有一个区间是可以把[1,4]包括在里面的
'''

# merge
# 56

def merge(intervals):
    if len(intervals) < 2:
        return intervals
    
    intervals = sorted(intervals, key = lambda x:x[0])

    new = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= new[-1][1]:
            new[-1][1] = max(end, new[-1][1])
        else:
            new.append([start, end])
    return new


# include or not
# 1288

def covered(A, intervals):
    for start, end in intervals:
        if A[0] >= start and A[1] <= end:
            return True
    return False


intervals = merge([[2, 4], [5, 6],[3,5]])
print(intervals)
print(covered([1, 4], intervals))
print(covered([2, 6], intervals))