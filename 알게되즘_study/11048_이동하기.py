import sys

dr = [1, 0, 1]
dc = [0, 1, 1]


def dfs(row, col, candy):
    global answer
    if answer > candy:
        return
    if row == N-1 and col == M - 1:
        answer = max(answer, candy)
        return

    for i in range(3):
        next_row = row + dr[i]
        next_col = col + dc[i]

        if not (0 <= next_row < N and 0 <= next_col < M):
            continue
        dfs(next_row, next_col, candy + MAP[next_row][next_col])


N, M = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
dfs(0, 0, MAP[0][0])
print(answer)