import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
prime_sum = 0
prime_min = 987654321

for number in range(M, N+1):
    if number > 1:
        prime = True
        # 최대 약수 어쩌구에 의해 제곱근까지만 검사하면 된다.
        sqrt_number = int(number ** 0.5)
        for i in range(2, sqrt_number + 1):
            if number % i == 0:
                prime = False
        if prime:
            prime_sum += number
            prime_min = min(prime_min, number)

if prime_sum > 0:
    print(prime_sum)
    print(prime_min)
else:
    print(-1)