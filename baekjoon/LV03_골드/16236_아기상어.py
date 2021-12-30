import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
MAP = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
answer = 0
shark_size = 2
shark_queue = []  # 상어 위치는 어차피 한번에 하나임
eaten_fish = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 물고기 개수와 아기 상어 위치 구하기
for r in range(N):
    for c in range(N):
        if MAP[r][c] == 9:
            shark_queue.append([r, c])

# 상어가 더 갈 곳이 없다면 먹을 생선도 없다는 뜻. 엄마 불러
while shark_queue:
    # 상어 위치 변동
    shark = shark_queue.pop()
    shark_row, shark_col = shark[0], shark[1]

    min_distance = 987654321
    small_fish = []
    visited = [[0]*N for _ in range(N)]
    visited[shark_row][shark_col] = 1

    # 상어가 움직여볼 곳을 저장하는 덱
    move_queue = deque()
    # 일단 상어 위치로부터 시작한다.
    move_queue.append([shark_row, shark_col])
    # 먹을 수 있는 생선들 찾기
    while move_queue:
        now = move_queue.popleft()
        now_row, now_col = now[0], now[1]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]
            # 아직 정해지지 않은 가상의 거리 값
            distance = visited[now_row][now_col] + 1
            # distance = abs(next_row-shark_row) + abs(next_col-shark_col)

            if 0 <= next_row < N and 0 <= next_col < N:
                # 제일 가까운 거리가 구해졌는데 더 멀면 이제 볼 필요가 없다.
                if min_distance != 987654321 and min_distance < distance:
                    continue
                # 이미 방문했으면 지나가세용
                if visited[next_row][next_col]:
                    continue
                # 같거나 작으면 일단 지나갈 수는 있다.
                if MAP[next_row][next_col] <= shark_size:
                    move_queue.append([next_row, next_col])
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    # 더 작아서 먹을 수 있는데 제일 가깝다면
                    if 0 < MAP[next_row][next_col] < shark_size and distance <= min_distance:
                        min_distance = distance
                        small_fish.append([next_row, next_col])

    # 먹을 수 있는 생선들이 있다면
    if small_fish:
        # 제일 위쪽(row), 왼쪽(col)을 기준으로 정렬하고
        small_fish.sort()

        eaten_row, eaten_col = small_fish[0][0], small_fish[0][1]
        # 생선 먹음
        MAP[eaten_row][eaten_col] = 0
        eaten_fish += 1
        # visited가 1부터 추가되기 때문에 매번 먹을때마다 1초가 더 추가되는 형태다.
        answer += (min_distance - 1)
        # 덱 초기화하고 현재 상어 위치 바꾸기기
        shark_queue.append([eaten_row, eaten_col])
        MAP[shark_row][shark_col] = 0
        # 만약 먹은 생선 수가 상어 크기와 같다면 상어 크기 키움
        if eaten_fish == shark_size:
            shark_size += 1
            eaten_fish = 0

print(answer)