T = int(input())

# 40보다 작거나 같은 자연수 또는 0
# 어차피 같은 값을 출력해야하니까 테케마다 새로 만들 필요가 없다.
DP = list([0, 0] for _ in range(41))

DP[0], DP[1] = [1, 0], [0, 1]

for i in range(2, 41):
    DP[i] = [DP[i-1][0] + DP[i-2][0], DP[i-1][1] + DP[i-2][1]]


for tc in range(T):
    N = int(input())
    print(' '.join(map(str, DP[N])))