A, B, C = map(int, input().split())

# 조건을 너무 어렵게 잡았었다...
if C > B:
    N = A // (C - B)
    print(N + 1)
else:
    print(-1)