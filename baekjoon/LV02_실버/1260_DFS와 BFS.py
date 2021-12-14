import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
node_connect = list([] for _ in range(N + 1))  # 연결된 노드 확인


# DFS 검색
def dfs(now_node):
    dfs_answer.append(now_node)
    node_visited[now_node] = 1

    for next_node in node_connect[now_node]:
        if node_visited[next_node]:
            continue
        dfs(next_node)

    return ' '.join(list(map(str, dfs_answer)))


# BFS 검색
def bfs():
    bfs_deque = deque()
    bfs_deque.append(V)
    bfs_answer = []

    # deque(방문할 노드들의 queue)에 요소가 있다면
    while bfs_deque:
        # 현재 보는 노드를 정하고 방문 처리
        now_node = bfs_deque.popleft()
        bfs_answer.append(now_node)

        # 다음에 갈 수 있는 노드들을 보면서
        for next_node in node_connect[now_node]:
            # 이미 방문한 노드라면 넘어가고
            if node_visited[next_node]:
                continue
            # 방문하지 않았다면 방문할 목록에 추가
            node_visited[next_node] = 1
            bfs_deque.append(next_node)

    return ' '.join(list(map(str, bfs_answer)))


# 인접 리스트 생성
for route in range(M):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    node_connect[nodeA].append(nodeB)
    node_connect[nodeB].append(nodeA)

for node_list in node_connect:
    node_list.sort()  # 작은 정점 번호 순으로 방문해야 하니까

dfs_answer = []
node_visited = [0] * (N + 1)  # 방문한 노드 처리
node_visited[V] = 1
print(dfs(V))
node_visited = [0] * (N + 1)  # 방문한 노드 처리
node_visited[V] = 1
print(bfs())