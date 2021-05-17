'''
中文计数：数字 + 单位
万以及万以下： 直接单位乘以前面的那个数字就好

亿到万或者超过亿：不能只是单纯的单位乘以前面的数字，还需要再乘上万或者亿


                 unit                           height_unit
一 - 千           < 1000                            1
万 - 千万         10 * 10000 / 100 * 10000...       10000
亿 - 万亿         

1. 考虑万，亿单位
2. 考虑万亿单位
 

'''


def cn2number(s):
    # corner case
    if not s:
        return -1

    # create dic
    # 数字映射
    number_map = {
        "零": 0,
        "一": 1,
        "二": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9
    }

    # 单位映射
    unit_map = {
        "十": 10,
        "百": 100,
        "千": 1000,
        "万": 10000,
        "亿": 100000000
    }

    count = 0
    unit = 1
    heigh_unit = 1

    for i in range(len(s) - 1, -1, -1):
        curr = s[i]
        if curr in number_map:
            count += unit * number_map[curr]

        elif curr in unit_map:
            '''
            temp = unit_map[curr]
            if temp >= 10000:
                # 万亿
                if heigh_unit == 10 ** 8:
                    heigh_unit = heigh_unit * temp
                    unit = heigh_unit
                else:
                    # 万, 亿
                    heigh_unit = temp
                    unit = heigh_unit
            else:
                if temp > unit:
                    unit = temp
                else:
                    unit = heigh_unit * temp
            '''
            new_unit = unit_map[curr]
            if new_unit >= 10000:
                # 万，亿
                if heigh_unit == 1 or heigh_unit == 10000:
                    heigh_unit = new_unit
                # 万亿
                else:
                    heigh_unit *= new_unit
                unit = heigh_unit
            # 累积
            else:
                unit = heigh_unit * new_unit
            

        else:
            return -1
    return count

res = cn2number("一百二十三")
print(res)
res = cn2number("一千二百三十四万五千六百七十八")
print(res)
res = cn2number("一亿二千三百四十五万六千七百八十一")
print(res)
res = cn2number("一千二百三十四万五千六百七十八亿一千二百三十四万五千六百七十八")
print(res)

'''
123
12345678
123456781
1234567812345678
'''