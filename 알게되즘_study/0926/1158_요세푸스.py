from collections import deque
# N, K = map(int, input().split())
N, K = 7, 3
table = deque()
answer = []

for i in range(1, N + 1):
    table.append(i)

print("<", end="")
while table:
    for _ in range(K):
        table.append(table.popleft())
    if len(table) == 1:
        print(table.pop(), end="")
    else:
        print(table.pop(), end=", ")
print(">", end="")