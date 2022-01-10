import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for tc in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * N for _ in range(M)]
    cabbages = []

    for _ in range(K):
        row, col = map(int, sys.stdin.readline().split())
        cabbages.append([row, col])
        field[row][col] = 1

    visited = [[0] * N for _ in range(M)]
    q = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    answer = 0

    # BFS
    for cabbage in cabbages:
        row, col = cabbage[0], cabbage[1]

        if not visited[row][col]:
            visited[row][col] = 1
            q.append([row, col])

            while q:
                now = q.popleft()
                now_row, now_col = now[0], now[1]

                for i in range(4):
                    next_row = now_row + dr[i]
                    next_col = now_col + dc[i]

                    if 0 <= next_row < M and 0 <= next_col < N:
                        if visited[next_row][next_col] or field[next_row][next_col] == 0:
                            continue
                        visited[next_row][next_col] = 1
                        q.append([next_row, next_col])

            answer += 1

    print(answer)
