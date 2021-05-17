'''
T级别文件，M级别内存空间，全排序

B -> KB -> MB -> GB -> TB
'''

'''
外部排序之多路归并
http://data.biancheng.net/view/76.html
https://wizardforcel.gitbooks.io/the-art-of-programming-by-july/content/06.04.html


比如说有1TB

1. 把1TB的文件分成1000分，每分约1GB
2. 再分1000分，每分约1MB
3. 依次对这1MB的数据进行排序
4. 进行归并
'''