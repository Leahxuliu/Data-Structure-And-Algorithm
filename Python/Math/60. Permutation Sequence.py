'''
找规律 DFS
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # def find(seq):
        #     if len(self.res) == k:
        #         return

        #     if len(seq) == n:
        #         self.res.append(''.join(seq))
        #         return

        #     for i in range(1, n + 1):
        #         if str(i) not in seq:
        #             seq.append(str(i))
        #             find(seq)
        #             seq.pop()
        #     return 

        def find(target):
            if len(self.res) == n:
                return 
            
            part = count[n - len(self.res) - 1]
            num = 0
            # choose the last number
            if target == 0:
                num = 1
            # find the part
            else:
                num = target // part
                if target % part != 0:
                    num += 1
                target -= part * (num - 1)

            temp = 0
            for i in range(1, n + 1):
                if i not in self.res:
                    temp += 1
                    if temp == num:
                        self.res.append(i)
                        break
            find(target)
            return
    
        count = [1]
        last = 1
        for i in range(1, n + 1):
            last *= i
            count.append(last)

        self.res = []
        find(k)
        return ''.join([str(each) for each in self.res])

