import sys

K = int(sys.stdin.readline().rstrip())
answer = []

for i in range(K):
    number = int(sys.stdin.readline().rstrip())
    if number == 0:
        answer.pop()
    else:
        answer.append(number)

print(sum(answer))