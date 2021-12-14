import sys

N = int(sys.stdin.readline().rstrip())
numbers = []
# 입력 받고
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

numbers.sort()
min_num = numbers[0]
# 모든 수에서 가장 작은 수 만큼을 뺀다.
for i in range(N):
    numbers[i] -= min_num


# 최대공약수 구하는 함수
def get_gcd(a, b):
    if b == 0:
        return a
    c = a % b
    return get_gcd(b, c)


gcd = 0
for i in range(N-1):
    gcd = get_gcd(gcd, numbers[i + 1])


# get answers - 최대 공약수의 약수들 저장하기
def get_divisor(n):
    divisors = []
    divisors_back = []

    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            if i != 1:
                divisors.append(i)
            if i != n // i:
                divisors_back.append(n // i)

    return divisors + divisors_back[::-1]


answers = get_divisor(gcd)
print(' '.join(map(str, answers)))