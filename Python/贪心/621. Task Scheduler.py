'''
贪心+heap

n+1为一个单位
不够的就拿空来补上
使用的字母是顺序是出现次数多到少
'''

from collections import defaultdict, Counter
from heapq import *
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        N = n + 1
        taskCount = Counter(tasks)
        heap = []
        for task, times in taskCount.items():
            heappush(heap, (-times, task))
        
        res = 0
        nums = len(tasks)

        while nums > 0:
            n = N
            temp = []
            while n > 0 and nums > 0:
                if len(heap) == 0:
                    res += n 
                    n = 0
                else:
                    times, task = heappop(heap)
                    if times + 1 < 0:
                        temp.append((times + 1, task))
                    res += 1
                    nums -= 1
                    n -= 1

            heap = heap + temp
            #heappush(heap, temp) wrong
            temp = []

        return res


'''
贪心
完成所有任务的最短时间取决于出现次数最多的任务数量。

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.

因为相同任务必须要有时间片为 n 的间隔，所以我们先把出现次数最多的任务 A 安排上（当然你也可以选择任务 B）。例子中 n = 2，那么任意两个任务 A 之间都必须间隔 2 个单位的时间：


A -> (单位时间) -> (单位时间) -> A -> (单位时间) -> (单位时间) -> A
中间间隔的单位时间可以用来安排别的任务，也可以处于“待命”状态。当然，为了使总任务时间最短，我们要尽可能地把单位时间分配给其他任务。现在把任务 B 安排上：


A -> B -> (单位时间) -> A -> B -> (单位时间) -> A -> B
很容易观察到，前面两个 A 任务一定会固定跟着 2 个单位时间的间隔。最后一个 A 之后是否还有任务跟随取决于是否存在与任务 A 出现次数相同的任务。

该例子的计算过程为：


(任务 A 出现的次数 - 1) * (n + 1) + (出现次数为 3 的任务个数)，即：

(3 - 1) * (2 + 1) + 2 = 8

所以整体的解题步骤如下：

计算每个任务出现的次数
找出出现次数最多的任务，假设出现次数为 x
计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count
特殊情况
然而存在一种特殊情况，例如：


输入: tasks = ["A","A","A","B","B","B","C","C","D","D"], n = 2
输出: 10
执行顺序: A -> B -> C -> A -> B -> D -> A -> B -> C -> D
此时如果按照上述方法计算将得到结果为 8，比数组总长度 10 要小，应返回数组长度


'''

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounter = Counter(tasks)
        
        max_times = taskCounter.most_common(1)[0][1]
        res = (max_times - 1) * (n + 1)  # 易错

        for times in taskCounter.values():
            if times == max_times:
                res += 1

        return res if res >= len(tasks) else len(tasks)
