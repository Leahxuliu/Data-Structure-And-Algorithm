'''
two pointer - sliding window

[0, 1, 2, 2]          count: 1, 2, 3, 2
i   i                 dict: {0:0, 1:1, 2:1}
j   j  j  j           res = 3

1. set i, j start at 0, 0
2. use count to stroe how many values in tree[i, j+1]
   use dict to stroe the value and the times, eg {0:1,1:1....}
3. if count > 2, i += 1
    else j += 1
    during each time, restore res, keep the max(j - i + 1)
4. when j move to the end, return res

time complexity:O(N) N is the number of trees
space complexity:O(1)

'''
from collections import defaultdict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if tree == []:
            return 0
        
        i = 0
        count = 0
        tree_info = defaultdict(int)
        res = 0
        
        for j, each_t in enumerate(tree):
            if tree_info[each_t] > 0:
                tree_info[each_t] += 1
            else:
                count += 1
                tree_info[each_t] += 1
            
            while count > 2:
                tree_info[tree[i]] -= 1
                if tree_info[tree[i]] == 0:
                    count -= 1
                i += 1
            
            res = max(res, j - i + 1)
        return res