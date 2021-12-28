import sys
N = int(sys.stdin.readline().rstrip())
adj = []

for _ in range(N):
    adj.append(list(map(int, sys.stdin.readline().split())))


for mid in range(N):
    for start in range(N):
        for end in range(N):
            # 바로 갈 수 있거나, 중간에 거쳐 갈 수 있다면
            if adj[start][end] or (adj[start][mid] and adj[mid][end]):
                adj[start][end] = 1

for line in adj:
    print(*line)