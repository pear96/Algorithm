import sys

T = int(sys.stdin.readline().rstrip())

for tc in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    apt = [[0] * 15 for _ in range(15)]
    apt[0] = [i for i in range(1, 16)]

    for floor in range(1, 15):
        for room in range(15):
            room_now = 0
            while room_now <= room:
                apt[floor][room] += apt[floor-1][room_now]
                room_now += 1

    print(apt[k][n-1])