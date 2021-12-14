import sys
from collections import deque

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    # 3차원 배열을 사용해야한다.
    visited = [[[0] * 2 for _ in range(M)] for __ in range(N)]
    # visited의 3번째가 0 이면 이미 부숴놓은거고, 1이면 부술 수 있는 것이다.
    visited[0][0][1] = 1

    while queue:
        now = queue.popleft()
        now_row, now_col, punchable = now[0], now[1], now[2]
        # 끝까지 가면 답이고 아니라면 -1
        if now_row == N - 1 and now_col == M - 1:
            return visited[now_row][now_col][punchable]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]
            if 0 <= next_row < N and 0 <= next_col < M:
                # 벽인데 부술 수 있다면 간다.
                if MAP[next_row][next_col] == 1 and punchable == 1:
                    visited[next_row][next_col][0] = visited[now_row][now_col][1] + 1
                    queue.append([next_row, next_col, 0])
                # 벽이 아닌데 간 적이 없다면 간다.
                elif MAP[next_row][next_col] == 0 and visited[next_row][next_col][punchable] == 0:
                    visited[next_row][next_col][punchable] = visited[now_row][now_col][punchable] + 1
                    queue.append([next_row, next_col, punchable])

    return -1  # 끝까지 못 갔으면

print(bfs())