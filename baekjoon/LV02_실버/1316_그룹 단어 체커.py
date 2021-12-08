"""
연속하지 않은 조건? = 내 앞의 문자와 다르고 + 이미 등장한 적이 있다.
앞의 문자를 확인한다는 점에서 첫 번째 인덱스만 따로 처리하면 되지 않을까
"""
import sys
input = sys.stdin.readline


N = int(input())
answer = 0  # 그룹 단어의 개수 저장

for _ in range(N):
    word = input().rstrip()  # 첫 단어를 받아온다.
    group_word = True  # 일단 그룹 단어가 맞다고 본다.
    visited = [False] * 26  # 알파벳 개수만큼 방문 배열 생성
    visited[ord(word[0])-ord('a')] = True  # word[0]: 첫 글자의 / ord(): 숫자화로 index 활용 / visited에 True
    for idx in range(1, len(word)):
        index = ord(word[idx]) - ord('a')  # 또ord 로 인덱스 계산해준다. 소문자만 나오니까 ord('a')를 뺀다.
        if visited[index] and word[idx-1] != word[idx]:  # 그룹 단어가 아닌 조건
            group_word = False  # 그룹 단어가 아니다
            break
        visited[index] = True  # 그 조건에 안걸렸다면 방문 표시
    if group_word:  # break해버리고 조건 안걸면 그룹 단어 아니더라도 정답이 증가하기 때문에
        answer += 1

print(answer)
