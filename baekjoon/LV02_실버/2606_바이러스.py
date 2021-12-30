"""
2606 바이러스
"""
import sys
from collections import deque

computer = int(sys.stdin.readline().rstrip())
pairs = int(sys.stdin.readline().rstrip())
network = [[] for _ in range(computer + 1)]
visited = [0] * (computer + 1)
queue = deque()
answer = 0

for i in range(pairs):
    start, end = map(int, sys.stdin.readline().split())
    network[start].append(end)
    network[end].append(start)

queue.append(1)
visited[1] = 1

while queue:
    now = queue.popleft()
    for next in network[now]:
        if not visited[next]:
            visited[next] = 1
            answer += 1
            queue.append(next)

print(answer)