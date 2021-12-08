import heapq
import sys

case = 1
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
input = sys.stdin.readline


def dij():
    queue = []
    heapq.heappush(queue, (MAP[0][0], 0, 0))
    distance[0][0] = 0

    while queue:
        now = heapq.heappop(queue)
        now_cost = now[0]
        now_row = now[1]
        now_col = now[2]

        if now_row == N - 1 and now_col == N - 1:
            print(f"Problem {case}: {distance[N - 1][N - 1]}")
            break

        for i in range(4):
            next_row = now_row + dr[i]
            next_col = now_col + dc[i]

            if 0 <= next_row < N and 0 <= next_col < N:
                next_cost = now_cost + MAP[next_row][next_col]

                if next_cost < distance[next_row][next_col]:
                    distance[next_row][next_col] = next_cost
                    heapq.heappush(queue, (next_cost, next_row, next_col))


while True:
    N = int(input())
    if N == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(N)]
    distance = [[987654321] * N for _ in range(N)]
    dij()
    case += 1
