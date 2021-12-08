"""
투포인터... start와 end 포인터를 계속 움직이기
리스트에서 첫 번째(i)를 찍고, 두 번째(j)부터 합을 구해나가는데
그 합이 M이면 answer + 1 하고 break
그 합이 M 초과면 break
그 합이 M 미만이면 계속 더해
"""
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

length = len(numbers)
numbers_sum = 0
answer = 0
next_idx = 0

for idx in range(length):
    while numbers_sum < M and next_idx < length:
        numbers_sum += numbers[next_idx]
        next_idx += 1
    if numbers_sum == M:
        answer += 1
    numbers_sum -= numbers[idx]

print(answer)
