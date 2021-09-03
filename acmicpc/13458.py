import sys

N = int(sys.stdin.readline())  # 시험장 수
A = list(map(int, sys.stdin.readline().split()))  # 각 시험장의 응시자 수
B, C = map(int, sys.stdin.readline().split())  # B = 총감독이 커버하는 수, C = 부감독 한명이 커버하는 수
answer = 0  # 필요한 감독관 수의 최솟값

for i in range(N):
    if A[i] <= B:
        answer += 1
    else:
        quotient, remainder = divmod(A[i]-B, C)
        if remainder:
            answer += 1 + quotient + 1
        else:
            answer += 1 + quotient

print(answer)