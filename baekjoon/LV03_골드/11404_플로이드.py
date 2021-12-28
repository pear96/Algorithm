import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = list([0] * N for _ in range(N))

for bus in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    a, b = a-1, b-1
    if graph[a][b] == 0 or graph[a][b] > c:
        graph[a][b] = c

for mid in range(N):
    for start in range(N):
        for end in range(N):
            if start == mid:
                break
            if start == end:
                continue
            if mid == end:
                continue
            if 1 <= graph[start][end] <= 100000 and 1 <= graph[start][mid] <= 100000 and 1 <= graph[mid][end] <= 100000:
                if graph[start][end] > graph[start][mid] + graph[mid][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end]
            elif graph[start][end] == 0 and graph[start][mid] and graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]


for line in graph:
    print(*line)
