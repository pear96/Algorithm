N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
answer = 0

for i in range(N):
    # 점수를 조작한다.
    scores[i] = (scores[i] / max_score) * 100
    # 조작한 점수를 합한다.
    answer += scores[i]
# 조작한 점수의 평균을 낸다.
print(answer / N)