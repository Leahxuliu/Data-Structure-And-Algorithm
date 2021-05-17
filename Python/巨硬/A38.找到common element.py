'''
两个list，怎么获得两个list当中的common element
'''

A = [1,1,2,3]
B = [1,2,5]
ans = set(A) & set(B)
print(ans)