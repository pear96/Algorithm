import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

MAP = list([list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H))
visited = list(list(list(0 for _ in range(M)) for _ in range(N)) for _ in range(H))

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

queue = deque()
riped = 0
fresh = 0
empty = 0
answer = 0

for h in range(H):
    for r in range(N):
        for c in range(M):
            if MAP[h][r][c] == 1:
                queue.append([h, r, c])
                riped += 1
            if MAP[h][r][c] == 0:
                fresh += 1
            if MAP[h][r][c] == -1:
                empty += 1


def bfs():
    global fresh
    global answer

    while queue:
        now = queue.popleft()
        now_height, now_row, now_col = now[0], now[1], now[2]

        for d in range(6):
            next_height = now_height + dh[d]
            next_row = now_row + dr[d]
            next_col = now_col + dc[d]

            if 0 <= next_row < N and 0 <= next_col < M and 0 <= next_height < H:
                if visited[next_height][next_row][next_col]:
                    continue
                if MAP[next_height][next_row][next_col] == 0:
                    visited[next_height][next_row][next_col] = visited[now_height][now_row][now_col] + 1
                    queue.append([next_height, next_row, next_col])
                    fresh -= 1
                    if answer < visited[next_height][next_row][next_col]:
                        answer = visited[next_height][next_row][next_col]


# 만약 모두 익은 토마토라면
if (riped + empty) == M * N * H:
    print(0)
else:
    bfs()
    if fresh:
        print(-1)
    else:
        print(answer)