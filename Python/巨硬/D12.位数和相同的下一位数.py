'''
给定一个十进制数x，其所有位数的和是k，
要求找到最小的、比x大的、并且位数和也等于k的数。x可以很大，以字符串形式给出。返回也要是字符串
'''

'''
从右往左扫
# 找到第一个不是0的num，该位置上的数-1，前一位+1
321 -> 330
330 -> 402

若前一位是9
191 --> 209
