'''
给定一个按照字典序列的string字符串数组，每个字符串表示一个int，要求按照string对应的int大小重新排序
'''
# change into dict, sort

a = {'a':10, 'b':2, 'c': 5}

sorted_a = sorted(a.keys(), key = lambda x:a[x])
print(sorted_a)