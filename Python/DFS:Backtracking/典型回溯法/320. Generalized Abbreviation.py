'''
backtracking

递归深度 * 每次递归临时变量的size = 空间复杂度 
时间复杂度: O(2 ^ n)
空间复杂度: O(n ^ 2)
'''
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        if word == '':
            return ['']
        
        def find(start, path, last):
            if start == len(word):
                # res.append(''.join([str(each) for each in path]))
                res.append(''.join(path))
                return

            # letter
            find(start + 1, path + [word[start]], False)
            # change to digit
            if path != [] and last:
                temp = path[-1]
                path[-1] = str(int(temp) + 1)
                find(start + 1, path, True)
                path[-1] = temp
            else:
                find(start + 1, path + ['1'], True)
            return
        
        res = []
        find(0, [], False)
        return res