from collections import defaultdict

seq_set = set()
for elem in seqs:
    for i in elem:
        seq_set.add(i)

indegree = defaultdict(int)
for elem in seq_set:
    indegree[elem] = 0  # 必须要写，不然入度为0的就没有了

outdegree = defaultdict(list)
for elem in seqs:
    for i in range(0, len(elem) - 1):
        indegree[elem[i + 1]] += 1
        outdegree[elem[i]].append(elem[i + 1])


sorted 与 sort的区别