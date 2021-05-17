'''
文件1有两列，p和k string类型，用\t隔开
文件2有两列，p1,p2,,,pn和k1,k2,,,kn 每列多个字符串，用逗号隔开，两列之间用\t隔开
输出文件2中包含文件1的所有行
比如文件1有一行p1k1,文件2有一行p1p3k1k2,这一行就要输出
'''

import sys
from collections import defaultdict
f1 = open('./f1.tsv', 'r')
f2 = open('./f2.tsv', 'r')

def save_file(f):
    info = defaultdict(set)
    for line in f:
        line = line.rstrip('\n')
        data = data.split('\t')
        # p:[k]
        info[data[0]].append(data[1])
    
    return info

if __name__ == "__main__":
    f1_info = save_file(f1)

    for line in f2:
        line = line.rstrip('\n')
        data = data.split('\t')

        p = data[0].split(',')
        f = set(data[1].split(','))

        for each_p in p:
            if each_p in f1_info:
                for each_f in f1_info[each_p]:
                    if each_f in f:
                        print(line)
                        break
    
                
                    