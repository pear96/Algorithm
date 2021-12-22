import sys

# 하 쓸데없이 복잡하게 생각해서 다 망했넹 ㅠㅠ
# 못 풀 난이도는 아니었는데...
# 그냥 보여준 코드에서 memoiztion만 구현해주면 되는거였다.
# a, b, c 모두 다 0 ~ 20까지만 계산할 필요가 있다.
DP = [[[0]*21 for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    # 0보다 작으면 1로 리턴해주고
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # 20보다 크면 20으로 통일하기 때문에
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if DP[a][b][c]:
        return DP[a][b][c]
    if a < b < c:
        DP[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return DP[a][b][c]
    DP[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return DP[a][b][c]


while True:
    a, b, c = map(int, sys.stdin.readline().split())

    # 입력 마지막
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")