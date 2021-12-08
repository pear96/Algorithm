import sys

X, Y = sys.stdin.readline().split()


def rev(str_number):
    reversed_number = str_number[::-1]
    return reversed_number


answer = int(rev(str(int(rev(X))+int(rev(Y)))))

print(answer)