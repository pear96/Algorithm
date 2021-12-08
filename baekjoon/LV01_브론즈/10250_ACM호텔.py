import sys

T = int(sys.stdin.readline().rstrip())

for tc in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    room = N // H + 1
    floor = N % H
    # floor H층일 때 0이 되어버림. 그리고 room은 1호가 더 뒤로 밀려남.
    if floor == 0:
        floor = H
        room -= 1
    print(f"{floor}{room:02}")

