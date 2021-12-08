import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs():
    while queue:
        now = queue.popleft()
        while relations[now]:
            next = relations[now].pop()
            if not visited[next]:
                visited[next] = visited[now] + 1
                queue.append(next)

N = int(sys.stdin.readline())  # 사람 수
targetA, targetB = map(int, sys.stdin.readline().split())  # 촌수 따져볼 두 사람
M = int(sys.stdin.readline())  # 관계의 수
visited = [0]*101
queue = deque()

relations = [[] for _ in range(101)]  # index = 부모, element = 자식
for i in range(M):  # 관계의 수만큼 돌면서 input 정리하기
    parent, child = map(int, sys.stdin.readline().split())
    relations[parent].append(child)
    relations[child].append(parent)

queue.append(targetA)
visited[targetA] = 1
bfs()

print(visited[targetB]-1)