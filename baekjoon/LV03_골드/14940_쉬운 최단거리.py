import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

goal = [0, 0]
unreachables = []

for row in range(N):
    for col in range(M):
        if MAP[row][col] == 2:
            goal = [row, col]
        elif MAP[row][col] == 0:
            unreachables.append([row, col])

visited = [[-1] * M for _ in range(N)]
queue = deque()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue.append([goal[0], goal[1]])
visited[goal[0]][goal[1]] = 0


while queue:
    now = queue.popleft()
    now_row, now_col = now[0], now[1]

    for i in range(4):
        next_row = now_row + dr[i]
        next_col = now_col + dc[i]

        if 0 <= next_row < N and 0 <= next_col < M:
            if visited[next_row][next_col] > 0:
                continue
            if MAP[next_row][next_col] == 0:
                continue
            if MAP[next_row][next_col] == 2:
                continue
            visited[next_row][next_col] = visited[now_row][now_col] + 1
            queue.append([next_row, next_col])

for (r, c) in unreachables:
    visited[r][c] = 0

for line in range(N):
    print(' '.join(map(str, visited[line])))
