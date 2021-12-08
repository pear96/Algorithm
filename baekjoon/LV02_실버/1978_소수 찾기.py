"""
소수는 수학에서 1과 그수 자신 이외의 자연수로는 나눌 수 없는, 1보다 큰 자연수이다.
"""
import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0

for number in numbers:
    prime = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                prime = False
        if prime:
            answer += 1
print(answer)