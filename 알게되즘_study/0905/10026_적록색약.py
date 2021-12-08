import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
painting = [list(sys.stdin.readline().rstrip()) for _ in range(N)]  # 그림을 2차원 배열로 받아온다.
# 적록색약일 떄와 아닐 때를 위해 2번 검사해야한다.

# 델타 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_section(r, c):
    stack = deque()  # 다음으로 갈 수 있는 위치를 저장하는 queue
    stack.append([r, c])  # 방문 안한 곳 부터 시작
    visited[r][c] = 1
    while stack:
        now = stack.popleft()
        now_row = now[0]
        now_col = now[1]
        now_color = painting[now_row][now_col]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if visited[next_row][next_col] != 0:
                continue
            if now_color != painting[next_row][next_col]:
                continue

            visited[next_row][next_col] = 1
            stack.append([next_row, next_col])


def find_section_rg(r, c):
    stack = deque()  # 다음으로 갈 수 있는 위치를 저장하는 queue
    stack.append([r, c])  # 방문 안한 곳 부터 시작
    visited[r][c] = 1
    while stack:
        now = stack.popleft()
        now_row = now[0]
        now_col = now[1]
        now_color = painting[now_row][now_col]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if visited[next_row][next_col] != 0:
                continue
            if now_color == 'B' and painting[next_row][next_col] != 'B':
                continue
            if now_color != 'B' and painting[next_row][next_col] == 'B':
                continue

            visited[next_row][next_col] = 1
            stack.append([next_row, next_col])


# 적록 색약이 아닐 때
visited = [[0] * N for _ in range(N)]  # 지나갔는지 확인하기 위하여
color = 0
for row in range(N):
    for col in range(N):
        if visited[row][col]:
            continue
        else:
            find_section(row, col)
            color += 1

# 적록 색약일 때
visited = [[0] * N for _ in range(N)]  # 지나갔는지 확인하기 위하여
rg_color = 0
for row in range(N):
    for col in range(N):
        if visited[row][col]:
            continue
        else:
            find_section_rg(row, col)
            rg_color += 1

print(color, rg_color)