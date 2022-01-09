import sys

V, M = map(int, sys.stdin.readline().split())

adj = []
ancestor = [i for i in range(V+1)]
answer = 0


def Find(node):
    if node == ancestor[node]:
        return node
    else:
        found_ancestor = Find(ancestor[node])
        ancestor[node] = found_ancestor
        return found_ancestor


def Union(a, b):
    ancestor[Find(b)] = Find(a)


for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    adj.append([cost, start, end])

adj.sort()

for node in adj:
    now_cost, now_start, now_end = node[0], node[1], node[2]

    if Find(now_start) != Find(now_end):
        answer += now_cost
        Union(now_start, now_end)


print(answer)