import sys

T = int(sys.stdin.readline())


for tc in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    cnt = 1

    if distance <= 3:
        answer = distance
    else:
        n = int(distance ** 0.5)
        if n ** 2 == distance:
            answer = 2 * n - 1
        elif n ** 2 < distance <= n ** 2 + n:
            answer = 2 * n
        else:
            answer = 2 * n + 1

    print(answer)
