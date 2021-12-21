import sys

N, M, B = map(int, sys.stdin.readline().split())
MAP = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

height = 0
limit = 1000000000000000000000000000000
time = 0

for i in range(257):
    max_h = 0
    min_h = 0
    for row in range(N):
        for col in range(M):
            if MAP[row][col] < i:
                min_h += (i - MAP[row][col])
            else:
                max_h += (MAP[row][col] - i)
    inven = max_h + B
    if inven < min_h:
        continue
    # 쌓는건 2초, 빼는건 1초
    time = 2 * max_h + min_h
    if time <= limit:
        limit = time
        height = i

print(time, height)