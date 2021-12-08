N = int(input())
num_string = input()
answer = 0

for idx in range(N):
    answer += int(num_string[idx])

print(answer)