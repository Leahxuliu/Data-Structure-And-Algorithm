'''
n克面粉，m种不同的粽子馅
第i种馅料有ai克，做i种粽子会消耗掉bi克馅料和ci克面粉，得到di的价值
不放馅料，消耗c0克面粉，得到d0价值

'''

'''
10  2  1  1     有10克面粉， 2种粽子馅，白粽子1克面粉，获利1； n  m  c0  d0
6   3  2  50    有6克馅料，每次用3克馅料，2克面粉，得到50；    a   b  c   d
8   2  1  10
'''


import sys

if __name__ == '__main__':

    try:
        mx = []
        while True:
            m = sys.stdin.readline().strip()
            #若是多输入，strip()默认是以空格分隔，返回一个包含多个字符串的list。
            if m == '':
                break
            m = list(m.split())
            mx.append(m)
        print(mx)
    except:
        pass

