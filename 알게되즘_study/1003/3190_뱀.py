from collections import deque
N = int(input())  # 보드 크기
K = int(input())  # 사과의 개수
MAP = [[0]*N for _ in range(N)] # 게임판 초기화

# 뱀 초기화
MAP[0][0] = 2  # 게임 시작하면 뱀이 있다. 뱀은 2
snake_direction = 'D'  # 처음 뱀의 방향은 D(오른쪽)이다.
delta_index = 0
head_row, head_col = 0, 0
tail_row, tail_col = 0, 0
snake_history = deque()
snake_history.append([0, 0])

# 게임 관련 초기화
apple = False
finish = False  # 게임이 끝났는지 판별할 변수
second = 0  # 걸린 시간
dr = [0, 1, 0, -1]  # 델타 배열 초기화. 동남서북
dc = [1, 0, -1, 0]

for _ in range(K):  # 맵에 사과 표시. 사과 있는곳은 1
    row, col = map(int, input().split())
    MAP[row-1][col-1] = 1

dir_change_dict = {}  # 뱀 방향 전환 딕셔너리
dir_change_count = int(input())  # 뱀이 방향을 바꾸는 횟수
for _ in range(dir_change_count):
    time, direction = input().split()
    time = int(time)
    dir_change_dict[time] = direction  # 딕셔너리에 '시간: 방향' 으로 저장


# 게임 시작!

while not finish:
    second += 1

    # 다음 위치 보면서
    next_row = head_row + dr[delta_index]
    next_col = head_col + dc[delta_index]

    if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N or MAP[next_row][next_col] == 2:
        finish = True # 게임이 끝나는 조건. 맵을 나가버렸거나 몸과 마주쳤거나.
        break

    if MAP[next_row][next_col] == 1: # 사과를 먹은 경우
        apple = True

    MAP[next_row][next_col] = 2  # 뱀이 지나간 자리
    snake_history.append([next_row, next_col])
    head_row, head_col = next_row, next_col  # 머리가 지나갔다.

    if not apple:  # 사과가 없다면
        tail = snake_history.popleft()
        tail_row = tail[0]
        tail_col = tail[1]
        MAP[tail_row][tail_col] = 0  # 있던 자리에서 떠나고
    apple = False

    # 초가 끝날 때 방향을 바꿔야하니까(원래는 second += 1 다음에 있었음)
    if second in dir_change_dict:  # 방향 바꿀 때가 되었다면
        snake_direction = dir_change_dict[second]
        if snake_direction == 'D':
            delta_index = (delta_index + 1) % 4  # 오른쪽일 경우 delta index 바꾸기 (0->1, 1->2, 2->3, 3->4)
        elif snake_direction == 'L':
            delta_index = (delta_index + 3) % 4  # 왼쪽일 경우 delta index 바꾸기 (0->3, 3->2, 2->1, 1->0)


print(second)


