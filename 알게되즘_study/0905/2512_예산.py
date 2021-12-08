#  지방 예산들의 합계가 총합을 넘지 않는 경우를 위해 상한가 찾는 작업을 함수로 뺐습니다.
def find_limit(min_limit, max_limit, regions):
    while min_limit <= max_limit:
        up_limit = (min_limit + max_limit) // 2
        region_sum = 0
        for region in regions:
            if region < up_limit:
                region_sum += region
            else:
                region_sum += up_limit
        if region_sum == budget:
            return up_limit
        elif region_sum > budget:
            max_limit = up_limit - 1
        else:
            min_limit = up_limit + 1
    return max_limit


N = int(sys.stdin.readline())
regions = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline())
max_budget = 0
answer = 0
regions_sum = 0

# 예산의 최소값(start)과 예산의 최대값(end) 찾기
for region in regions:
    if max_budget < region:
        max_budget = region
    regions_sum += region

if regions_sum <= budget:
    answer = max_budget
else:
    answer = find_limit(0, max_budget, regions)
    # 처음엔 start에 0이 아니라 min_budget으로 넣었는데 틀려서 반례를 찾아보니 지방의 최소 요구 예산보다 낮을 경우를 계산하지 못했습니다.
    # 총 예산이 100이고 각 4개의 지방마다 100을 원한다면 지방의 요구 예산 중 최소값이 100이더라도 정해진 예산은 25이겠죠.
    # 그러므로 min_budget은 필요 없는 변수가 됩니다.

print(answer)