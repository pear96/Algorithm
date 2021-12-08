A = int(input())
B = int(input())
C = int(input())

numbers = [0] * 10
result = str(A * B * C)

for i in range(len(result)):
    numbers[int(result[i])] += 1

for j in range(10):
    print(numbers[j])