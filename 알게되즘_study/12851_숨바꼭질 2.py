"""
https://cocook.tistory.com/111
"""

import sys
from collections import deque  # bfs를 위해 queue 사용
N, M = map(int, sys.stdin.readline().split())
visited = [0] * 1000001
case = [0] * 1000001
queue = deque()


def bfs():
    while queue:
        pos = queue.popleft()

        for next_pos in [pos - 1, pos + 1, pos * 2]:
            if 0 <= next_pos <= 100000:
                if not visited[next_pos]:
                    visited[next_pos] = visited[pos] + 1
                    case[next_pos] = case[pos]
                    queue.append(next_pos)
                else:
                    if visited[next_pos] == visited[pos] + 1:
                        case[next_pos] += case[pos]


queue.append(N)
visited[N] = 1
case[N] = 1
bfs()

print(visited[M] - 1)
print(case[M])