import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

visited = [0] * (N + 1)
connect = [[] for _ in range(N + 1)]
answer = 0
q = deque()


def bfs():
    while q:
        now = q.popleft()

        if not connect[now]:
            return

        for node in connect[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = 1


for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    connect[start].append(end)
    connect[end].append(start)


for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = 1
        q.append(i)
        bfs()
        answer += 1

print(answer)