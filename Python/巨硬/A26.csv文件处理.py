'''
一个逗号分割的csv文件，转化成二维矩阵

* 双引号里面有双引号
* 一行没有正常结束
* 两个，，
* \t\n
* ....
'''

import sys

f = open('patient.csv', 'r')
# f = open('test.tsv', 'r')

for line in f:
    line = line.rstrip('\n')
    data = line.split(',')
    print(data)