"""
https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/
최대값, 최소값을 관리하는 두 개의 힙 사용
각 숫자를 고유하게 판별할 수 있는 id (for문의 index)가 필요하다.
해당 값을 이미 삭제 했다면 (False라면) 힙에서 빼버린다. -> 진짜를 빼기 전 사전 작업
해당 값을 삭제하지 않았다면 (True라면) 힙에서 빼버린다.
왜냐하면 이미 min에서 빼버린거는 max에서도 빼야하기 때문이다. 반대도 마찬가지

다 보고 나서 아직 쓰레기값이 남아있을 수 있으므로 확실히 제거해준 다음에
max의 처음값에 -를 붙이고, min의 처음값을 출력하면 된다.
둘 다 비어있다면 empty!
"""
import heapq
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    min_heap = []
    max_heap = []
    visited = [False] * k

    for id in range(k):
        order = sys.stdin.readline().split()
        op, num = order[0], int(order[1])

        if op == 'I':
            heapq.heappush(min_heap, (num, id))
            heapq.heappush(max_heap, (-num, id))
            visited[id] = True
        elif num == 1:
            # 최대값들을 방문하지 않았다면
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            # 쓰레기값을 다 빼고나서 아직 최대값이 있다면
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        else:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                # 최솟값 삭제
                heapq.heappop(min_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")