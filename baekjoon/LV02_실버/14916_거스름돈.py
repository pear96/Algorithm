"""
J Hang joon
"""
# 입력
money = int(input())  # 거스름돈 액수

# dp
dp = [-1] * 100001
dp[2], dp[5] = 1, 1
for i in range(3, money + 1):
    if dp[i-2] != -1:  # 2원만 더하면 됨
        if dp[i-5] != -1:  # 5원만 더하면 됨
            dp[i] = min(dp[i-2] + 1, dp[i-5]) + 1
        else:
            dp[i] = dp[i-2] + 1
    else:
        if dp[i-5] != -1:  # 5원만 더하면 됨
            dp[i] = dp[i-5] + 1
        else:
            continue
print(dp[money])