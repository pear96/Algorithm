import sys

N, M, B = map(int, sys.stdin.readline().split())
# MAP = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
# 시간초과가 나서 다른 사람들 코드를 보니까 딕셔너리를 사용함
MAP = dict()

for i in range(N):
    heights = list(map(int, sys.stdin.readline().split()))
    for j in heights:
        if j in MAP:
            MAP[j] += 1
        else:
            MAP[j] = 1
# 걸릴 시간과 제일 높은 높이
answer_height = -1
answer_time = 1000000000000000000000000000000

# 구해놓은 높이 중에 가장 큰 높이와 가장 작은 높이를 구한다.
max_height = 0
min_height = 257
for height, count in MAP.items():
    if height >= max_height:
        max_height = height
    if height <= min_height:
        min_height = height

# min과 max를 구해놓고 나서 그 사이에서만 적절한 숫자를 하나 찾아본다.
for i in range(min_height, max_height + 1):
    inven = B
    time_sum = 0
    for height, count in MAP.items():
        if height < i:
            # 가방에서 블록을 빼는건 1초, 더 작은 높이 전부를 한번에 계산
            time_sum += (i-height) * count
            inven -= (i-height) * count
        # 여기서 elif 사용하면 더 느려진다고함. else보다 elif가 더 느리다. https://ggodong.tistory.com/297
        else:
            # 가방에 블록을 넣는건 2초, 같거나 더 큰 높이 전부를 한번에 계산
            time_sum += 2*(height - i)*count
            inven += (height - i)*count
    # 낮은것들을 올릴 수 없다면 될지 안될지 계산해 볼 필요가 없다.
    # 더 짧은 시간이 걸려야 한다.
    if inven >= 0 and time_sum <= answer_time and answer_height < i:
        answer_time = time_sum
        # 그리고 그 때의 최고 높이
        answer_height = i

print(answer_time, answer_height)