import sys
from collections import deque
sys.stdin = open('input.txt')


field = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
combo = 0
Finish = False


def find_set(r, c):
    puyo_set = deque()
    visited = [[0]*6 for _ in range(12)]
    puyo_set.append([r, c])
    visited[r][c] = 1
    while puyo_set:
        now = puyo_set.popleft()
        puyo_history.append(now)
        now_row = now[0]
        now_col = now[1]
        now_color = field[now_row][now_col]

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if next_row < 0 or next_col < 0 or next_row >= 12 or next_col >= 6:
                continue
            if now_color != field[next_row][next_col]:
                continue
            if visited[next_row][next_col] != 0 :
                continue
            puyo_set.append([next_row, next_col])
            visited[next_row][next_col] = 1


def clean_field():
    while puyo_history:
        now = puyo_history.popleft()
        now_row = now[0]
        now_col = now[1]
        field[now_row][now_col] = '.'


def gravity():
    for col in range(6):
        empty = 0
        for row in range(11, -1, -1):
            if field[row][col] == '.':
                empty += 1
            else:
                if empty > 0:
                    field[row + empty][col] = field[row][col]
                    field[row][col] = '.'


while not Finish:
    for row in range(12):
        for col in range(6):
            if field[row][col] == '.':
                continue
            else:
                puyo_history = deque()
                find_set(row, col)
                if len(puyo_history) >= 4:
                    clean_field()
                    combo += 1
                else:
                    puyo_history = deque()
    gravity()


print(combo)