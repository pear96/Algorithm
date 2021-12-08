import sys

N = int(sys.stdin.readline().rstrip())

kilo_5, kilo_3 = 0, 0

if N == 4 or N == 7:
    print(-1)
elif N % 5 == 0:
    print(N // 5)
else:
    if N % 10 == 1 or N % 10 == 6:
        kilo_3 = 2
        N -= 3 * kilo_3
        kilo_5 = N // 5
    if N % 10 == 2 or N % 10 == 7:
        kilo_3 = 4
        N -= 3 * kilo_3
        kilo_5 = N // 5
    if N % 10 == 3 or N % 10 == 8:
        kilo_3 = 1
        N -= 3 * kilo_3
        kilo_5 = N // 5
    if N % 10 == 4 or N % 10 == 9:
        kilo_3 = 3
        N -= 3 * kilo_3
        kilo_5 = N // 5
    print(kilo_3 + kilo_5)

