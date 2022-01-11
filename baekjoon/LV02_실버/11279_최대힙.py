import heapq
import sys

N = int(sys.stdin.readline().rstrip())
max_heap = []

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if max_heap:
            max_num = -heapq.heappop(max_heap)
            print(max_num)
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -x)