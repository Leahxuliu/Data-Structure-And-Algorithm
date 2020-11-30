class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if len(text) <= 1:
            return len(text)

        info = {}
        for i in text:
            if i in info:
                info[i] += 1
            else:
                info[i] = 1
        
        res = 0
        l, r = 0, 1
        used = False
        count = 1

        while r < len(text):
            if text[l] == text[r] and count < info[text[l]]:
                # 加count < info[text[l]]是因为会存在已经用过的情况，比如"aaabaaa"
                count += 1
                r += 1
                res = max(res, count)
            else:
                if used == False and count < info[text[l]]:
                    used = True
                    count += 1
                    r += 1
                    res = max(res, count)
                else:
                    res = max(res, count)
                    temp = text[l]
                    while l < len(text) and text[l] == temp:
                        l += 1 
                    r = l + 1
                    count = 1
                    used = False

        # "acbaaa" "aabbaba"
        if count < info[text[r - 1]] and used == False:
            res = max(res, count + 1)
        
        return res