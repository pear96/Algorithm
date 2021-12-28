import sys
from collections import

computer = int(sys.stdin.readline().rstrip())
pairs = int(sys.stdin.readline().rstrip())
network = [[] for _ in range(computer)]

for i in range(pairs):
    start, end = map(int, sys.stdin.readline().split())
    network[start].append(end)
    network[end].append(start)

