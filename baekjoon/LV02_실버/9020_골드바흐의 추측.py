import sys

T = int(sys.stdin.readline().rstrip())

# 소수 체크 리스트 만들고
prime_check = [False, False] + [True] * (10000 - 1)
for number in range(2, 10001):
    if prime_check[number]:
        for i in range(number * number, 10001, number):
            prime_check[i] = False

# 진행
for tc in range(T):
    N = int(sys.stdin.readline().rstrip())
    prime_gap = 987654321
    answer_prime1, answer_prime2 = 0, 0

    for prime_one in range(2, N // 2 + 1):
        if prime_check[prime_one]:
            prime_two = N - prime_one
            if prime_check[prime_two]:
                if prime_gap > prime_two - prime_one:
                    answer_prime1, answer_prime2 = prime_one, prime_two

    print(answer_prime1, answer_prime2)