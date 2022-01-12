import sys

X = int(sys.stdin.readline().rstrip())
visited = [0] * (X + 1)

for i in range(2, X+1):
    # 1을 빼고 시작하는 이유는 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문
    visited[i] = visited[i - 1] + 1
    if i % 3 == 0:
        visited[i] = min(visited[i], visited[i // 3] + 1)
    if i % 2 == 0:
        visited[i] = min(visited[i], visited[i // 2] + 1)

print(visited[X])