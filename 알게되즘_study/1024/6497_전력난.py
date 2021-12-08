"""
최소신장트리 MST

"""
import sys
import heapq


while True:
    M, N = map(int, sys.stdin.readline().split())
    if M == 0 and N == 0:
        break
    total_cost = 0
    graph = [[] for _ in range(M + 1)]
    for i in range(N):
        start, end, cost = map(int, sys.stdin.readline().split())
        total_cost += cost
        graph[start].append((cost, end))
        graph[end].append((cost, start))

    queue = []
    visited = [False] * (M + 1)

    for data in graph[0]:
        heapq.heappush(queue, data)
    visited[0] = True

    min_cost = 0
    while queue:
        now = heapq.heappop(queue)
        now_cost = now[0]
        now_end = now[1]

        if visited[now_end]:
            continue
        min_cost += now_cost
        visited[now_end] = True

        for data in graph[now_end]:
            if visited[data[1]]:
                continue
            heapq.heappush(queue, data)

    print(total_cost - min_cost)