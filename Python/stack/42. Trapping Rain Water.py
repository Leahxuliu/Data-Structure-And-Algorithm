#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/06/28


'''
monostone
1. 对低洼的地方感兴趣，就可以使用一个单调递减栈，将递减的边界存进去，一旦发现当前的数字大于栈顶元素了，那么就有可能会有能装水的地方产生
2. 当前的数字是右边界
3. stack.pop 低坑的高度
4. stack[-1] 左边界
5. 接水的面积 = min(左边界高度，右边界高度) * （左边界 - 右边界 - 1）
              如果左右边界里面右0，则是0
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return 0
        
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                low = height[stack.pop()]
                if len(stack) > 0:
                    temp = (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - low)
                    if temp > 0:
                        res += temp
            stack.append(i)
        return res