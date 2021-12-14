from collections import deque

# 입력 받기
N, M = map(int, input().split())
MAP = [list(map(int, input().rstrip())) for _ in range(N)]

# 전역 변수
queue = deque()
reachable_walls = list()
answer = list()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_breakable_walls():
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while queue:
        now = queue.popleft()
        now_row, now_col = now[0], now[1]

        if now_row == N - 1 and now_col == M - 1:
            return

        for i in range(4):
            # 상하좌우를 보면서
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            # 맵 밖이라면 넘어간다
            if 0 > next_row or N <= next_row or 0 > next_col or M <= next_col:
                continue
            # 이미 방문한 곳이라면 넘어간다
            if visited[next_row][next_col]:
                continue
            # 벽인데,
            if MAP[next_row][next_col]:
                if MAP[now_row][now_col]:
                    continue
                else:
                    reachable_walls.append([next_row, next_col])
            else:
                queue.append([next_row, next_col])
                visited[next_row][next_col] = 1


def bfs(break_wall):

    while queue:
        # 현재 위치
        now = queue.popleft()
        now_row, now_col = now[0], now[1]

        for i in range(4):
            # 상하좌우를 보면서
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            # 맵 밖이라면 넘어간다
            if 0 > next_row or N <= next_row or 0 > next_col or M <= next_col:
                continue
            # 이미 방문한 곳이라면 넘어간다
            if visited[next_row][next_col]:
                continue
            # 벽인데,
            if MAP[next_row][next_col]:
                # 아직 벽을 안뚫어봤으면 벽을 뚫어본다.
                if next_row == break_wall[0] and next_col == break_wall[1]:
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    queue.append([next_row, next_col])
                else:
                    continue
            # 길이라면,
            else:
                visited[next_row][next_col] = visited[now_row][now_col] + 1
                queue.append([next_row, next_col])


# 도달할 수 있는(부숴볼 수 있는) 벽 BFS로 찾기
queue.append([0, 0])
find_breakable_walls()

# 도달할 수 있는 벽 하나당 BFS 돌려보기
for wall in reachable_walls:
    queue.append([0, 0])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    bfs(wall)
    if visited[N-1][M-1]:
        answer.append(visited[N-1][M-1])
    queue.clear()

if answer:
    print(min(answer))
else:
    print(-1)