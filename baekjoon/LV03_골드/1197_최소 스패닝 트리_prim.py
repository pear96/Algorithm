import heapq
import sys

V, M = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(V+1)]
heap = []
visited = [False] * (V+1)
answer = 0

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    adj[start].append((cost, end))
    adj[end].append((cost, start))

# 시작점에 연결된 애들부터 넣어주면 되는거였는데!!! 왜 이걸 다 넣으려고 해갖곤!
for node in adj[1]:
    heapq.heappush(heap, node)
visited[1] = True

while heap:
    now = heapq.heappop(heap)
    cost, end = now[0], now[1]

    if visited[end]:
        continue
    # 방문 안했으면 추가하면 되는 거였어...
    answer += cost
    visited[end] = True
    for next_node in adj[end]:
        heapq.heappush(heap, next_node)

print(answer)