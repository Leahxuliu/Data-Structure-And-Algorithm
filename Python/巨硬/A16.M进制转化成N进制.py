'''
多进制 -> 十进制
123
(1 x 7 + 2) x 7 + 2

十进制 -> 多进制
123 
余数倒过来

注意符号
'''

def change(integer, M, N):
    if integer == 0:
        return '0'

    flag = ''
    if integer < 0:
        flag = '-'

    num = str(abs(integer))

    # change into 10x
    num10 = 0
    for i in num:
        num10 = num10 * M + int(i)

    # change into N
    num10 = num10
    res = ''
    while num10 != 0:
        reminder = num10 % N 
        res = str(reminder) + res 
        num10 = num10 // N 

    
    return flag + res

print(change(101, 2, 4))


      