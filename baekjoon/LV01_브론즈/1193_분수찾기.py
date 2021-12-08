X = int(input())

index = 1  # 군수열 - 1군, 2군, 3군...

while True:
    now_group_first_idx = 1 + index * (index - 1) // 2  # 현재 군의 첫 번째 index
    next_group_first_idx = 1 + index * (index + 1) // 2   # 다음 군의 첫 번째 index
    if now_group_first_idx <= X < next_group_first_idx:  # 지금 숫자가 속한 군을 찾아내고
        if index % 2:  # 홀수 군이라면 분자 감소, 분모 증가
            numerator = next_group_first_idx - X  # 다음 군 첫 번째 index - 현재 군 첫 번째 index = 개수차이
            denominator = 1 + X - now_group_first_idx  # 원하는 index - 현재 군 첫 번째 index + 1
        else:
            numerator = 1 + X - now_group_first_idx  # 홀수일 때와 반대
            denominator = next_group_first_idx - X
        print(f"{numerator}/{denominator}")
        break
    index += 1