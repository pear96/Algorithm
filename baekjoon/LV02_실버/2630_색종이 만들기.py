import sys

N = int(sys.stdin.readline().rstrip())
paper = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

blue, white = 0, 0


def check(size, row, col):
    global blue, white
    if size == 1:
        if paper[row][col] == 1:
            blue += 1
        else:
            white += 1
    else:
        count = 0
        for i in range(row, row + size):
            for j in range(col, col + size):
                count += paper[i][j]
        if count == 0:
            white += 1
        elif count == size * size:
            blue += 1
        else:
            half = size // 2
            for r in range(2):
                for c in range(2):
                    check(half, row + r*half, col + c*half)

check(N, 0, 0)
print(white)
print(blue)