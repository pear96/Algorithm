import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
people = deque(list(i for i in range(1, N + 1)))
josephus = [0] * N
remove_cnt = 0

while people:
    idx = 1
    while idx < K:
        people.append(people.popleft())
        idx += 1
    josephus[remove_cnt] = people.popleft()
    remove_cnt += 1

print(f"<{', '.join(map(str, josephus))}>")