import sys

N, M = map(int, sys.stdin.readline().split())
MAP = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

d1r = [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1]
d1c = [1, 1, 0, 1, 0, -1, -1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0]
d2r = [1, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0, 0, 1, 1]
d2c = [0, 2, 0, 2, 1, 0, 0, 1, -1, 1, 0, 0, 0, 0, 1, 2, 2, 1, -1]
d3r = [1, 0, 3, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1]
d3c = [1, 3, 0, 1, 0, 0, 1, 1, -1, 2, -1, 1, -1, 0, 1, 0, 2, 2, -2]

answer = 0

for row in range(N):
    for col in range(M):
        now = MAP[row][col]
        for i in range(19):
            d1_row, d1_col = row + d1r[i], col + d1c[i]
            d2_row, d2_col = row + d2r[i], col + d2c[i]
            d3_row, d3_col = row + d3r[i], col + d3c[i]
            if 0 <= d1_row < N and 0 <= d1_col < M and\
                0 <= d2_row < N and 0 <= d2_col < M and\
                0 <= d3_row < N and 0 <= d3_col < M:
                tetromino = now + MAP[d1_row][d1_col] + MAP[d2_row][d2_col] + MAP[d3_row][d3_col]
                if answer < tetromino:
                    answer = tetromino

print(answer)
