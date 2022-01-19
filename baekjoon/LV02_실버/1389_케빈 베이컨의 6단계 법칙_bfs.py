"""
내가 푼게 아님
cchanggu00
"""


def bfs(x):
    total = 0
    queue = [x]
    while queue:
        x = queue[0]
        del queue[0]
        for i in list(graph[x]):
            if not visited[i]:
                visited[i] = visited[x] + 1
                total += visited[i]
                queue.append(i)
    return total


n, m = map(int, input().split())
graph = list(set() for _ in range(n + 1))

for _ in range(m):
    temp = list(map(int, input().split()))
    graph[temp[0]].add(temp[1])
    graph[temp[1]].add(temp[0])

min = 5000 * 100
min_index = 0
for i in range(1, n + 1):
    visited = [0 for _ in range(n + 1)]
    result = bfs(i)
    if result < min:
        min = result
        min_index = i
print(min_index)