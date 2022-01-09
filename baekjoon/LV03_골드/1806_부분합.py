import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
answer = 100000

front_idx = 0
now_idx = 0
temp_sum = nums[front_idx]

while front_idx < N:
    now_length = now_idx - front_idx + 1
    if temp_sum >= S:
        if now_length < answer:
            answer = now_length
        temp_sum -= nums[front_idx]
        front_idx += 1
    else:
        if now_idx < N:
            if now_idx == N - 1 and front_idx < N:
                temp_sum -= nums[front_idx]
                front_idx += 1
            else:
                now_idx += 1
                temp_sum += nums[now_idx]

if answer == 100000:
    print(0)
else:
    print(answer)