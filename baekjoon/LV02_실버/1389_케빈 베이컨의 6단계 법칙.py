import sys

N, M = map(int, sys.stdin.readline().split())
relation = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    if relation[A][B]:
        continue
    else:
        relation[A][B] = 1
        relation[B][A] = 1

for mid in range(1, N+1):
    for start in range(1, N+1):
        if start == mid:
            continue
        for end in range(1, N+1):
            if start == end or end == mid:
                continue
            if relation[start][mid] == 0 or relation[mid][end] == 0:
                continue
            if relation[start][end] == 0:
                relation[start][end] = relation[start][mid] + relation[mid][end]
            if relation[start][end] > relation[start][mid] + relation[mid][end]:
                relation[start][end] = relation[start][mid] + relation[mid][end]

kevin = list()

for idx in range(1, N+1):
    kevin.append((sum(relation[idx]), idx))

kevin.sort()

print(kevin[0][1])