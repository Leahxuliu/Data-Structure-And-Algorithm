from heapq import heappop, heappush

heap = []

heappush(heap, (2, 0))
heappush(heap, (2, -1))

print(heappop(heap))