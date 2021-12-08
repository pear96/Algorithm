N = int(input())

DP = [0] * 1001

DP[0] = 1
DP[1] = 3

for i in range(2, N + 1):
    DP[i] = DP[i-1] + DP[i-2] * 2

print(DP[N - 1] % 10007)