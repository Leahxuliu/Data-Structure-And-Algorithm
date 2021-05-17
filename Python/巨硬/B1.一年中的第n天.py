'''
YYYYMMDD 一年中的第n天

四年一闰，百年不闰，四百年再闰
'''

def find_day(year, num):
    '''
    find ith day in the year
    '''
    data = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30}
    # no_leap = {'01': 0, '02': 31, '03': 59, ....}

    flag = ''
    # check year
    if year % 400 == 0:
        flag = 'leap'
    elif year % 100 != 0 and year % 4 == 0:
        flag = 'leap'
    

    if flag == 'leap':
        data['02'] = 29
    
    count = 0
    for k, v in data.items():
        if count + v >= num:
            day = num - count 
            return '%s-%d' % (k, day)
        count += v
    return

            



res = find_day(2021, 32)
print(res)
