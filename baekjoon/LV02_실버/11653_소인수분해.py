"""
소수 리스트 미리 만들고 풀어야하는줄 알고 풀다가 시간 날렸네ㅠㅠ
"""
import sys

N = int(sys.stdin.readline().rstrip())
prime = 2
while N > 1:
    while N % prime == 0:
        print(prime)
        N /= prime
    prime += 1