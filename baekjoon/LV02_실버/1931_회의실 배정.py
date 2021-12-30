import sys

N = int(sys.stdin.readline().rstrip())
meetings = []
answer = 0

for idx in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append([start, end])

meetings.sort()
meetings = sorted(meetings, key=lambda meeting : meeting[1])

last_time = 0

for start, end in meetings:
    if start >= last_time:
        answer += 1
        last_time = end

print(answer)