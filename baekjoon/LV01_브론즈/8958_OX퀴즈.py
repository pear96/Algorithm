T = int(input())

for tc in range(T):
    quiz_result = input()
    answer = 0 # 총 점수 합
    count = 0 # 연속으로 O 맞은 수
    for result in quiz_result:
        if result == 'O':
            count += 1
        else:
            count = 0
        answer += count

    print(answer)