"""
https://www.acmicpc.net/source/35012476
"""
T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    child = 1
    mom = 1
    for j in range(k+1):
        child *= (n+j)
        mom *= (j+1)

    print(int(child/mom))