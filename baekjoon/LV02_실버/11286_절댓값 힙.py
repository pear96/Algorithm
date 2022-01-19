"""
짧은 풀이
if x:
    hq.heappush(min_heap, (abs(x), x))
else:
    print(hq.heappop(min_heap)[1] if min_heap else 0)

"""
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if heap:
            min_heap = heapq.heappop(heap)
            sign = min_heap[1]
            if sign == 1:
                print(min_heap[0])
            else:
                print(-min_heap[0])
        else:
            print(0)
    else:
        if num < 0:
            heapq.heappush(heap, (-num, -1))
        else:
            heapq.heappush(heap, (num, 1))

