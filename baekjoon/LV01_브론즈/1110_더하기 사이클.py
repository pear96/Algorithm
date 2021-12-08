"""
왜 while True인거로만 풀어야하는 문제만 내는지 모르겟다...
1. 조건을 len(N) < 2 일때로 해서 문제가 있었다.
2. int(N) > 10 해버려서 10이 포함이 안되어서 입력예시에 1이 무한루프 걸렸었다.
"""
import sys
input = sys.stdin.readline

N = input().rstrip()
start = N
count = 0

while True:
    if int(N) > 9:
        sum_char = str(int(N[0]) + int(N[1]))
    else:
        sum_char = '0' + N

    N = N[-1] + sum_char[-1]
    count += 1
    if int(N) == int(start):
        break

print(count)