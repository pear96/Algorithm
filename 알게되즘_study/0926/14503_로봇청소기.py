import sys
sys.stdin = open('../input.txt')

N, M = map(int, input().split())
row, col, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

answer = 1
finish = False
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


while not finish:
    MAP[row][col] = 2  # 청소

    # 네방향 다 안되더라
    if MAP[row - 1][col] != 0 and MAP[row][col + 1] != 0 and MAP[row + 1][col] != 0 and MAP[row][col - 1] != 0:
        if d == 0 and MAP[row + 1][col] != 1:
            row += 1
        elif d == 1 and MAP[row][col - 1] != 1:
            col -= 1
        elif d == 2 and MAP[row - 1][col] != 1:
            row -= 1
        elif d == 3 and MAP[row][col + 1] != 1:
            col += 1
        else:
            finish = True
            break

    for _ in range(4):
        d = (d + 3) % 4
        next_row = row + dr[d]
        next_col = col + dc[d]

        if 0 < next_row < N and 0 < next_col < M and MAP[next_row][next_col] == 0:
            row = next_row
            col = next_col
            answer += 1
            break  # 청소하게 for문 그만돌고 while 다음으로 돌아가, 아니면 방향 돌리고



print(answer)