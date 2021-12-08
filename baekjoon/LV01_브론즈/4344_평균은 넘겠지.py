T = int(input())

for tc in range(T):
    input_data = list(map(int, input().split()))
    N = input_data[0]
    scores = input_data[1:]

    # 평균 구하기
    avg_score = 0
    for score in scores:
        avg_score += score
    avg_score /= N

    # 평균 넘는 사람 수
    over_avg_cnt = 0
    for score in scores:
        if score > avg_score:
            over_avg_cnt += 1
    # 평균 넘는 사람 비율
    if over_avg_cnt == 0:
        print(f"{0:.3f}%")
    else:
        over_avg_ratio = round((over_avg_cnt / N) * 100, 3)
        print(f"{over_avg_ratio:.3f}%")

