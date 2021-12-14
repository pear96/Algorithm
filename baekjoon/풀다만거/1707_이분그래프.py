"""
내가 빨간색일 때 내 주변을 전부 파란색으로 칠할 수 있는지 본다.
하나라도 안된다면 그건 이분 그래프로 만들 수 없는 것이다.
"""

import sys
from collections import deque

K = int(sys.stdin.readline().rstrip())


def bfs(root_vtx):
    queue = deque()
    queue.append(root_vtx)
    visited[root_vtx] = 1

    while queue:
        now = queue.popleft()

        # 1번 부터 순차적으로 탐색하면서 visited를 가려고 하면 순회다.
        for next_vtx in vertices[now]:
            # 아직 방문하지 않았다면
            if visited[next_vtx] == 0:
                # 지금 보는 점과 반대되는 값을 입력
                visited[next_vtx] = -visited[now]
                queue.append(next_vtx)
            else:
                # 방문했는데 나와 인접한 놈인데 나랑 같은 값이다 => 이분그래프 불가
                if visited[next_vtx] == visited[now]:
                    return False
    # 다 봤는데 나랑 인접한 곳에서 같은 값이 없었다면 이분그래프 만들 수 있다.
    return True

for tc in range(K):
    V, E = map(int, sys.stdin.readline().split())
    # nodes[1] : 1번 노드와 연결된 모든 노드 저장
    vertices = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    bipartite = True

    # 입력값 처리
    for i in range(E):
        u, v = map(int, sys.stdin.readline().split())
        # 무방향이라 양쪽 다 저장해주고
        vertices[u].append(v)
        vertices[v].append(u)

    for vertex in range(1, V + 1):
        if visited[vertex] == 0:
            if not bfs(vertex):
                bipartite = False
                break

    print('YES' if bipartite else 'NO')