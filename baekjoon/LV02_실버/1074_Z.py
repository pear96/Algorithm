N, row, col = map(int, input().split())
step = 0


while N != 0:
    N -= 1

    if row < 2 ** N and col < 2 ** N:
        step += ( 2 ** N ) * ( 2 ** N ) * 0
    elif row < 2 ** N <= col:
        step += (2 ** N) * (2 ** N) * 1
        col -= (2 ** N)
    elif row >= 2 ** N > col:
        step += (2 ** N) * (2 ** N) * 2
        row -= (2 ** N)
    else:
        step += (2 ** N) * (2 ** N) * 3
        row -= (2 ** N)
        col -= (2 ** N)

print(step)