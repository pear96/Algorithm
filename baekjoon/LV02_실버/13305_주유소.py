import sys

N = int(sys.stdin.readline().rstrip())
distance_list = list(map(int, sys.stdin.readline().split()))
cost_list = list(map(int, sys.stdin.readline().split()))
gas = [[0, 0] for _ in range(N)]

# [가격, 거리] 를 N-1 개만큼 만든다.
for idx in range(N-1):
    gas[idx][0] = cost_list[idx]
    gas[idx][1] = distance_list[idx]

# 다음 도시 가격이 같거나 더 비싸면 road를 늘린다. 싸면 거리를 초기화하고 답에 추가한다.
answer = 0
min_idx = 0
now_idx = 0
road = 0

# 최소가 끝을 가진 않을테니까
while now_idx < N:
    # 최소값이 더 작으면 거리만 늘려가면 된다.
    if gas[min_idx][0] <= gas[now_idx][0]:
        road += gas[now_idx][1]
        now_idx += 1
    else:
        # 지금까지 축적해온 거리 청산하고
        answer += gas[min_idx][0] * road
        # 지금 보는 애가 최소값이 되는 거고
        min_idx = now_idx
        # 거리는 now값
        road = gas[now_idx][1]
        # 이제 나는 최소값의 다음 부터 보겠지
        now_idx += 1



print(answer)