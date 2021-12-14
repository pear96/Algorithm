import sys
import heapq

N = int(sys.stdin.readline())
lesson_list = []

for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    lesson_list.append([S, T])

lesson_list.sort()

answer = []
heapq.heappush(answer, lesson_list[0][1])

for lesson in range(1, N):
    if lesson_list[lesson][0] < answer[0]:
        heapq.heappush(answer, lesson_list[lesson][1])
    else:
        # 이어서 하려면 힙에 있던 최소 값을 빼버리고 덧 씌운다.
        heapq.heappop(answer)
        heapq.heappush(answer, lesson_list[lesson][1])

print(len(answer))