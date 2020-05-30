# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/05/27

'''
Brute force
1. 用4个for遍历每一种时间
2. 遍历数字的同时，检查它是否可以显示在时钟上
3. 通过datetime计算时差， 每次更新最近的时间
    datetime.strptime(str,"%H:%M")

time O(N) N = 4 * 4 * 4 * 4种情况
space: O(1)

Backtracking
1. 用Backtracking遍历每一种时间
2. 遍历数字的同时，检查它是否可以显示在时钟上
3. 通过datetime计算时差， 每次更新最近的时间
    datetime.strptime(str,"%H:%M")


参考答案
1. set time的数，然后sort
2. 去四个值，形成newtime，如果newtime > time, return newtime
    （因为数值被sort完毕，所以遇到的第一个大于time的就是最接近的时间 )
3. 没有比time大的newtime，则数组当中，除0以外，最小的值 c*2 : c*2就是最接近的值
'''

class Solution:
    def nextClosestTime(self, time: str) -> str:
        if time == '00:00':
            return '00:00'

        time_list = sorted(list(set(time[:2] + time[-2:])))
        
        for i in time_list:
            for j in time_list:
                for n in time_list:
                    for m in time_list:
                        new_time = i + j + ':' + n + m
                        if new_time != time:
                            if new_time < '2400' and new_time[-2:] < '60' and new_time > time:
                                return new_time

        if time_list[0] != '0':
            return time_list[0]*2+':'+time_list[0]*2
        else:
            return time_list[1]*2+':'+time_list[1]*2
