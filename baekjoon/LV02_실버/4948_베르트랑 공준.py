import sys

while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    answer = 0
    primes_check = [False, False] + [True] * (2 * N - 1)
    for number in range(2, 2 * N + 1):
        if primes_check[number]:
            if number > N:
                answer += 1
            for idx in range(number * number, 2 * N + 1, number):
                primes_check[idx] = False

    print(answer)
