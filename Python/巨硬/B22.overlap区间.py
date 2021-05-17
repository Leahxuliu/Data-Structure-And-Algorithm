'''
定义一个点是vaild的，当覆盖在这个点上的interval数量不超过2个。求问，给一串intervals，最少删掉几个interval可以使所有点都是vaild
'''

def remove_overlap(intervals):
    if len(intervals) < 3:
        return 0

    intervals = sorted(intervals, key = lambda x:x[1])

    count = 0
    pre_end = intervals[0][1]
    overlap = -1

    for start, end in intervals[1:]:
        if start > pre_end:
            pre_end = end 
        else:
            if start <= overlap:
                count += 1
            else:
                overlap = pre_end
                pre_end = end
    return count


print(remove_overlap([[0, 2], [0, 3], [1, 3]]))