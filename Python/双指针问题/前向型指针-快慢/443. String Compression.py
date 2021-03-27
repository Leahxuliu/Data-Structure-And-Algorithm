'''
快慢双指针
在原本的list上进行替换
'''
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        
        l = 0
        r = 0
        count = 0
        chars.append('0')
        res = 0  # next res's index

        while r < len(chars):
            if chars[l] == chars[r]:
                count += 1
                r += 1
            else:
                # put char
                chars[res] = chars[l]
                res += 1
                # put times
                if count > 1:
                    for each in str(count):
                        chars[res] = each
                        res += 1

                l = r
                count = 0
    
        return res


        # if len(chars) < 2:
        #     return len(chars)
        
        # l = 0
        # r = 0
        # count = 0
        # res = 0
        # new = ''

        # while r < len(chars):
        #     if chars[l] == chars[r]:
        #         count += 1
        #         r += 1
        #     else:
        #         new += '%s%d' % (chars[l], count)
        #         l = r 
        #         count = 0
        
        # if l < len(chars):
        #     new += '%s%d' % (chars[l], count)
        
        # print(new)
        # return len(new)