# Greedy

# 1. 基本概念

- 在对问题求解时，总是做出在当前看来最好的选择。即 不从整体上最优加以考虑，它所做出的仅是在某种意义上的局部最优解。**当前状态下的最优解**
- 贪心算法只对部分问题才能得到整体最优解，选择的贪心策略必须具备无后效性。
- 

# 2. 分配问题

## 2.1 题型 

题目要求

- 将某些东西分配给具有某些要求的人
- 给两个list，分别是东西的属性和人的要求属性

题目思路

- 排序：对两个list进行排序
- 使用东西对人进行满足， 先满足一个，再满足下一个
  - 若满足，东西+ 1， 人+ 1
  - 若不满足，东西就 + 1

题目

**455 发饼干**

```python
# 贪心 + two point
# 时间复杂度 O(min(m, n))
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g == [] or s == []:
            return 
        
        g.sort()
        s.sort()
        
        i, j = 0, 0
        res = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:  # 关键点，不仅仅是等于的时候 
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res

```



**135 发糖**

```python
'''
1. 初始都是一颗糖
2. 从左往右遍历，i比i-1分数高，则i比i-1多一颗糖
3. 从右往左遍历，i比i+1分数高，则max(res[i], res[i + 1] + 1)
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if ratings == []:
            return 0

        n = len(ratings)
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                #res[i] = res[i + 1] + 1  # 错误 比如[1,3,4,5,2]， 从左到右扫完之后是[1,2,3,4,1],再从右往左扫时，倒是第二个变成了2
                res[i] = max(res[i], res[i + 1] + 1)
        return sum(res)    
```



# 3. 区间问题

**如何区分是左端点排序还是右端点排序**

- ending： 射气球，最大不相交
- starting： 其他all

## 3.1 ending排序 （杜绝「前面包后面」）

* 核心： **右端升序排序**，就杜绝了「前面包后面」的情况
  * 比如[[1,2], [2,3],[4,5],[1,5]]，这里的[1,5]包裹了全部

- 最大不相交区间（non-overlap)
  - 给定N个闭区间，选择若干区间，使得选中的区间之间互不相交（包括端点）。输出可选取区间的最大数量。
  - 实际问题：很多课程，或者活动，我们从中选择最多数量的课程或活动参加
  - 算法思路：跟区间选点一致（end排序）
  - 贪心证明：
    - 因为需要尽量多的独立的线段，所以每个线段都尽可能的小
    - 对于同一右端点，左端点越大，线段长度越小。
    - 要尽可能的多排，也就是意味着结束的越早越好，所以是ending排序
    - 为什么要对右端点进行排序呢？如果左端点进行排序，那么右端点是多少并不知道，那么每一条线段都不能对之前所有的线段进行一个总结，那么这就明显不满足贪心的结构了。

* 区间选点问题（射气球）
  * 给定N个闭区间[ai,bi]，请你在数轴上选择尽量少的点，使得每个区间内至少包含一个选出的点。输出选择的点的最小数量。位于区间端点上的点也算作区间内。
  * 实际问题：用最少的箭射爆所有气球
  * 算法思路：
    - 将所有区间按照右端点从小到大排序 （end排序）
    - 从前往后枚举每个区间
      如果当前区间已经包含点，直接pass 否则结果加一，选择当前区间的右端点，继续枚举后面的区间
  * 贪心证明：
    * **右端升序排序**，就杜绝了「前面包后面」的情况
* 只要知道是ending排序就好做

 

**435. Non-overlapping Intervals**

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == [] or intervals == []:
            return 0
        
        intervals = sorted(intervals, key = lambda x:x[1])

        pre_end = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start < pre_end:
                res += 1
            else:
                pre_end = end
        return res
```



**452. Minimum Number of Arrows to Burst Balloons**

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points == [] or points == [[]]:
            return 0
        
        points = sorted(points, key = lambda x:x[1])
        pre_end = points[0][-1]
        count = 1

        for start, end in points[1:]:
            if start <= pre_end:
                continue
            else:
                count += 1
                pre_end = end
        
        return count
```



## 3.2 starting排序 （包括「前面包后面」）

* 核心： **左端升序排序**，就包括了「前面包后面」的情况
  * 比如会议室，合并区间，都是要从start开始考虑包含情况

- 区间分组(会议室)
  - 给定N个闭区间，将这些区间分成若干组，使得每组内部的区间两两之间（包括端点）没有交集，并使得组数尽可能小。输出最小组数。
  - 实际问题：公司今天有20场会议，问最少用几个会议室可以安排下
  - 算法思路：
    - 将所有区间按照左端点从小到大排序（start排序）
    - 从前往后处理每个区间
      判断能否将其放到某个现有的组中（小顶堆维护右端点（最早结束的区间））

- 区间完全覆盖问题
  - 给定N个闭区间[ai,bi]以及一个线段区间[s,t]，请你选择尽量少的区间，将指定线段区间完全覆盖。输出最少区间数，如果无法完全覆盖则输出-1。
  - 算法思路：
    - 将所有区间按左端点从小到大排序（start排序）
    - 从前往后依次枚举每个区间，在所有能覆盖start的区间中选择右端点最大的，然后将start更新成右端点的最大值



**253.Meeting Rooms II**

```python
# heap + greedy
# heap里面放现在正在使用的会议室的结束时间
# 新会议开始的时候，是否有老的会议已经结束

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals == [] or intervals == [[]]:
            return 0

        intervals = sorted(intervals, key = lambda x:x[0])
        end_heap = [intervals[0][1]]
        res = 1
        
        for start, end in intervals[1:]:
            pre_end = heappop(end_heap)
            if start >= pre_end:
                heappush(end_heap, end)
            else:
                heappush(end_heap, pre_end)
                heappush(end_heap, end)
                res = max(res, len(end_heap))
        
        return res

```



**56. Merge Intervals**

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals = sorted(intervals, key = lambda x:x[0])
        merged_intervals = [intervals[0]]
        
        for start, end in intervals[1:]:
            temp = merged_intervals[-1][1]
            if start <= temp:
                merged_intervals[-1][1] = max(end, temp)
            else:
                merged_intervals.append([start, end])
        
        return merged_intervals
```



**986. Interval List Intersections (区间问题-找交集) 不是贪心 是双指针**

```python
# 分3种情况，一前一后，有交集（pointer移动end在前的），一后一前

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if A == [] or B == []:
            return []
        
        i = 0
        j = 0
        res = []

        while i < len(A) and j < len(B):
            s1, e1 = A[i]
            s2, e2 = B[j]

            # A前 B后 无交集
            if e1 < s2:
                i += 1
            
            # 有交集（pointer移动end在前的）
            elif e1 >= s2 and s1 <= e2:
                res.append([max(s1, s2), min(e1, e2)])
                if e1 < e2:
                    i += 1
                elif e1 > e2:
                    j += 1
                else:
                    i += 1
                    j += 1
            
            # A后 B前 无交集
            else:
                j += 1
        
        return res
```







# 4. 跳跃游戏







# 5. 贪心+heap

