numbers = [0] * 42
answer = 0

for _ in range(10):
    quotient = int(input()) % 42
    if not numbers[quotient]:
        numbers[quotient] += 1
        answer += 1

print(answer)

