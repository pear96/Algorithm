import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
danji = 0
houses = []


# 집이 몇채나 연결되어있는지 확인하기
def bfs(row, col):
    queue = deque()
    queue.append([row, col])
    visited[row][col] = 1
    house_cnt = 1

    while queue:
        now = queue.popleft()
        now_row, now_col = now[0], now[1]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if 0 <= next_row < N and 0 <= next_col < N:
                # 이미 간 곳이면 볼 일 없다.
                if visited[next_row][next_col]:
                    continue
                else:
                    # 집이 있는 곳이면 계속 탐색
                    if MAP[next_row][next_col]:
                        visited[next_row][next_col] = 1
                        queue.append([next_row, next_col])
                        house_cnt += 1
                    # 집이 없는 곳이면 방문하지 않도록 -1 처리
                    else:
                        visited[next_row][next_col] = -1
    houses.append(house_cnt)


# 단지인지 확인하기
for r in range(N):
    for c in range(N):
        if visited[r][c]:
            continue
        elif MAP[r][c]:
            bfs(r, c)
            danji += 1
        else:
            # 집이 없는 곳이라서 넘어가게
            visited[r][c] = -1

print(danji)
houses.sort()
for house in houses:
    print(house)