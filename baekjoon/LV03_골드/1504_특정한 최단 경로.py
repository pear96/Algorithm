import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
# 각 정점과 연결된 (거리, 정점)을 저장한다. 양방향 그래프
graph = [[] for _ in range(N + 1)]


def dijkstra(start):
    dist = [sys.maxsize] * (N + 1)
    q = []
    # 1번 정점에서 부터 시작하니까
    heapq.heappush(q, (0, start))
    # 이거 안해줘서 84%에서 틀림
    dist[start] = 0

    while q:
        # 아직 확정하지 않은 점들 중 가장 가까운 점
        now = heapq.heappop(q)
        min_num = now[1]
        min_dist = now[0]

        for cost, to in graph[min_num]:
            if min_dist + cost >= dist[to]:
                continue
            dist[to] = min_dist + cost
            heapq.heappush(q, (dist[to], to))
    # return값이 하나의 숫자가 아니고 배열 자체를 준다.
    return dist


for _ in range(E):
    from_vtx, to_vtx, cost = map(int, sys.stdin.readline().split())
    graph[from_vtx].append((cost, to_vtx))
    graph[to_vtx].append((cost, from_vtx))
mid1, mid2 = map(int, sys.stdin.readline().split())

# 시작점부터의 거리 모음
path_1 = dijkstra(1)
# mid1부터의 거리 모음
path_mid1 = dijkstra(mid1)
# mid2부터의 거리 모음
path_mid2 = dijkstra(mid2)

# 1부터 mid1까지 + mid1부터 mid2까지 + mid2부터 N까지
result1 = path_1[mid1] + path_mid1[mid2] + path_mid2[N]
# 1부터 mid2까지 + mid2부터 mid1까지 + mid1부터 N까지
result2 = path_1[mid2] + path_mid2[mid1] + path_mid1[N]

result = min(result1, result2)

if result >= sys.maxsize:
    print(-1)
else:
    print(result)
