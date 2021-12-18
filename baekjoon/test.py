import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
answers = [-1] * N
stack = []

for number in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        popped = stack.pop()
        answers[popped] = numbers[i]
    stack.append(i)

print(' '.join(map(str, answers)))
