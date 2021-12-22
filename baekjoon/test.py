import sys

# a = 1, b = 2, c = 4
# -50 ~ 50은 101개
# 7 * 101

DP = [1] * (101*101*101)

for c in range(1, 51):
    for b in range(1, 51):
        for a in range(1, 51):
            if a > 20 or b > 20 or c > 20:
                DP[a + 2 * b + 4 * c] = DP[140]
                continue
            if a < b < c:
                DP[a + 2 * b + 4 * c] = DP[a + 2 * b + 4 * (c - 1)] + DP[a + 2 * (b - 1) + 4 * (c - 1)] - DP[
                    a + 2 * (b - 1) + 4 * c]
                continue
            DP[a + 2 * b + 4 * c] = DP[(a - 1) + 2 * b + 4 * c] + DP[(a - 1) + 2 * (b - 1) + 4 * c] \
                                    + DP[(a - 1) + 2 * b + 4 * (c - 1)] - DP[(a - 1) + 2 * (b - 1) + 4 * (c - 1)]


print(DP[7])
print(DP[14])
print(DP[42])
print(DP[350])