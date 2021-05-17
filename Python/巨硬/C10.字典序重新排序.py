'''
给定一个按照字典序列的string字符串数组，每个字符串表示一个int
要求按照string对应的int大小重新排序
'''
from collections import Counter


def sort(string, data):
    if string == "":
        return ""
    
    data = sorted(data.items(), key = lambda x:x[1])

    count = Counter(string)

    new = ''
    for char, value in data:
        if char in count:
            new += char * count[char]
    
    return new


a = 'bcdgz'
data = {'b': 10, 'c':3, 'd': 2, 'g':11, 'z':12}
print(sort(a, data))


'''
题意理解有误
有待确认

'''