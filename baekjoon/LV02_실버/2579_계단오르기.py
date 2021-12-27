import sys

N = int(sys.stdin.readline().rstrip())

stairs = [0] * 301
DP = [0] * 301
answer = 0

for i in range(N):
    stairs[i] = int(sys.stdin.readline().rstrip())

# i번 까지의 계단 값 중 제일 높은 거
DP[0] = stairs[0]
DP[1] = stairs[0] + stairs[1] # 아니면 stairs[1]인데 0번째도 합한게 무조건 크니까
# 2번째 계단까지 갈 수 있는 2가지의 방법 중 값이 더 많이 나오는 걸로 저장
DP[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

for i in range(3, N):
    # 내 전 계단을 밟고 온 값과 내 전전 계단을 밟고 온 값 비교
    DP[i] = max(DP[i-3]+stairs[i-1]+stairs[i], DP[i-2]+stairs[i])

print(DP[N-1])