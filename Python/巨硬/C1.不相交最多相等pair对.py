'''
一个数组，两个相邻数相加和相同的数组，最多几组；不能重复选

* dictionary里面保存两两相加的所有情况，key是sum，value是pair对的index
* 从len(value)最大的开始，数最大不相交的线段数量
'''
from collections import defaultdict 
def count_max_pair(arr):
    if arr == []:
        return 0

    info = defaultdict(list) 
    for i, each in enumerate(arr):
        if i == len(arr) - 1:
            continue
        info[each + arr[i + 1]].append((i, i + 1))
    
    info = sorted(info.items(), key = lambda x:len(x[1]))

    res = 0
    for k, v in info:
        if res > len(v):
            break
        
        v = sorted(v, key =lambda s:s[1])
        end = v[0][1]
        count = 0
        for i in range(1, len(v)):
            # 若是数成立的个数，那么count的起始值是1！
            #     if v[i][0] > end:
            #         count += 1
            #         end = v[i][1]
            # res = max(res, count)
            if v[i][0] <= end:
                count += 1
            else:
                end = v[i][1]
        res = max(res, len(v) - count)
    
    return res

a = count_max_pair([10, 1, 3, 1, 2, 2, 1, 0, 4])
print(a)

a = count_max_pair([5,3,1,3,2,3])
print(a)

a = count_max_pair([9,9,9,9,9])
print(a)