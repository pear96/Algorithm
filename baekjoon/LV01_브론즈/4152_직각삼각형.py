import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    triangle = False
    if a == 0 and b == 0 and c == 0:
        break
    if a ** 2 + b ** 2 == c ** 2:
        triangle = True
    elif a ** 2 + c ** 2 == b ** 2:
        triangle = True
    elif b ** 2 + c ** 2 == a ** 2:
        triangle = True

    if triangle:
        print('right')
    else:
        print('wrong')