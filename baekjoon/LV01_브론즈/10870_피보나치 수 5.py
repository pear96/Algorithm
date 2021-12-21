import sys

N = int(sys.stdin.readline().rstrip())


def fibo(num):
    if num > 1:
        return fibo(num-1) + fibo(num-2)
    elif num == 0:
        return 0
    else:
        return 1


print(fibo(N))