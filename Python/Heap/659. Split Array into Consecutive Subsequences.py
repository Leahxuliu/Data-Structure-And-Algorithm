'''

还是贪心算法，从头扫描，如果能接着上一个序列，就在上个序列后添加当前值，如果不行，前插一行继续下一个数字。
例如 2， 3， 4， 4， 5， 5， 6
顺序如下
[[2]]
[[2, 3]]
[[2, 3, 4]]
4不能后接，前插一行
[[4], [2, 3, 4]]
[[4, 5], [2, 3, 4]]
[[4, 5], [2, 3, 4, 5]]
[[4, 5, 6], [2, 3, 4, 5]]
最后比较是否所有序列长度大于等于3
'''

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        res = []
        for n in nums:
            for v in res:
                if n == v[-1] + 1:
                    v.append(n)
                    break
            else:
                res.insert(0, [n])

        return all([len(v) >= 3 for v in res])




'''
dict + heap
1. 用dictionary来记录分段情况，key是integer，value（list， 因为有多种）是以key这个intger为end的段里有几个数
2. 遍历nums （i）
    a. 如果dict[i-1] == [], 也就是意味着i只能开新段，所以这一段是1 （ 注意要用heap来加入，这样才能确保下次pop的时候是最小值）
    b. 如果dict[i-1]是存在的，那么选择最短的一段往上加
3. 遍历dictionary里面的value，看是否大于3

时间复杂度：O(nlogn)，其中 n = nn 是数组的长度。

'''

from collections import defaultdict
from heapq import *

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = defaultdict(list)

        for i in nums:
            if count[i - 1] == []:
                heappush(count[i], 1)
                # count[i].append(1)  wrong count[i][0]不是最小值

            else:
                min_len = heappop(count[i - 1])
                # count[i].append(min_len + 1)
                heappush(count[i], min_len + 1)

        for each in count.values():
            if len(each) > 0 and each[0] < 3:
                return False
        return True


'''
时间复杂度：O(n)

贪心
1. 把每个数值出现的次数储存到dict里
2. 遍历nums（x），同时用一个dict储存以改字母结尾的序列个数
3. 如果x-1存在序列个数，x-1的序列个数-1，x的序列个数+1，x的出现次数-1
4. 如果x-1不存在序列个数
    如果有可以使用的x+1，x+2，x+2的序列个数+1，x，x+1,x+2的出现次数-1
    如果不能构成长度为3的序列，则return false
'''

from collections import Counter, defaultdict
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = Counter(nums)
        seqCount = Counter()  # 这里用Counter要比defaultdict要好，因为是按照value大小排好序的

        for x in nums:
            if countMap[x] == 0:
                continue
                
            if seqCount[x - 1] >= 1:
                seqCount[x - 1] -= 1
                seqCount[x] += 1
                countMap[x] -= 1
            else:
                if countMap[x + 1] >= 1 and countMap[x + 2] >= 1:
                    seqCount[x + 2] += 1
                    countMap[x] -= 1
                    countMap[x + 1] -= 1
                    countMap[x + 2] -= 1
                else:
                    return False
        return True
        
