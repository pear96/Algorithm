import sys
from collections import deque
#  많이 풀었던 BFS
#  맵에 특정 지을게 없어서 오히려 visited를 새로 만들 필요가 없었다.
#  그래서 board를 visited로 사용했다.
T = int(sys.stdin.readline())

dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, -2, -1, 1, 2]

for tc in range(T):
    size = int(sys.stdin.readline())
    board = [[0]*size for _ in range(size)]  # visited
    start_row, start_col = map(int, sys.stdin.readline().split())
    goal_row, goal_col = map(int, sys.stdin.readline().split())
    positions = deque()
    positions.append([start_row, start_col])
    board[start_row][start_col] = 1

    while positions:
        now = positions.popleft()
        now_row = now[0]
        now_col = now[1]
        if now_row == goal_row and now_col == goal_col:
            break
        for i in range(8):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                continue
            if board[next_row][next_col] != 0:
                continue

            positions.append([next_row, next_col])
            board[next_row][next_col] = board[now_row][now_col] + 1

    print(board[goal_row][goal_col]-1)

