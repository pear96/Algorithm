import sys

N = int(sys.stdin.readline().rstrip())

minutes = list(map(int, sys.stdin.readline().split()))

minutes.sort()

answer = minutes[0]

for idx in range(1, N):
    minutes[idx] += minutes[idx-1]
    answer += minutes[idx]

print(answer)