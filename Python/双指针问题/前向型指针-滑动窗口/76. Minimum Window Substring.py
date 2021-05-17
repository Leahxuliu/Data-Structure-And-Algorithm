'''
1. move right until all characters in t are included into s
2. move left, until count != 0

滑动窗口
right去找需要的，直到count == 0，然后看left能不能缩小
注意这里的count，只计算t里存在的内容，
也就是在right指针移动的时候，info[s[right]] > 0，count-= 1
left指针移动的时候，info[s[left]] == 0, count += 1; 因为info[s[left]] < 0的时候，left挪动并不影响

相似题 567
567因为要完全一样所以用count就很复杂，改用dictionary
同样本题如果用dicionary就会变得很复杂，因为窗口内的东西不一样要与t完全相同

滑动窗口基础题 209

'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '' or s == '':
            return ''
        
        info = {}
        for i in t:
            if i in info:
                info[i] += 1
            else:
                info[i] = 1
        
        res = [0, len(s)]
        count = len(t)

        left = 0
        for right in range(len(s)):
            if s[right] in info:
                if info[s[right]] > 0:
                    count -= 1
                info[s[right]] -= 1
                
            while count == 0:
                if right - left < res[1] - res[0]:
                    res = [left, right]
                
                if s[left] in info:
                    if info[s[left]] == 0:
                        count += 1
                    info[s[left]] += 1
                left += 1

        return s[res[0]:res[1] + 1] if res != [0, len(s)] else ""

