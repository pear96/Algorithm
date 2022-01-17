import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def solution(size, row, col):
    color = paper[row][col] # 현재 구역 기준 0,0 과 값이 같은지 보려구
    for i in range(row, row+size):
        for j in range(col, col+size):
            if color != paper[row][col]:
                half = size//2
                # 1 사분면
                solution(half, row, col)
                # 2 사분면
                solution(half, row, col+half)
                # 3 사분면
                solution(half, row+half, col)
                # 4 사분면
                solution(half, row+half, col+half)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(N, 0, 0)
print(result.count(0))
print(result.count(1))