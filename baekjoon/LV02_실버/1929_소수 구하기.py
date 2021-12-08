import sys

M, N = map(int, sys.stdin.readline().split())
prime_check = [False, False] + [True] * (N - 1)

for number in range(2, N + 1):
    if prime_check[number]:
        if number >= M:
            print(number)
        for i in range(number * number, N + 1, number):
            prime_check[i] = False