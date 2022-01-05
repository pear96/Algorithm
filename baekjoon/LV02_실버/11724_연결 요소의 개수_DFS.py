import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

visited = [0] * (N + 1)
connect = [[] for _ in range(N + 1)]
answer = 0


def dfs(now):
    if not connect[now]:
        return
    if visited[now]:
        return

    visited[now] = 1

    for node in connect[now]:
        if not visited[node]:
            dfs(node)


for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    connect[start].append(end)
    connect[end].append(start)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)