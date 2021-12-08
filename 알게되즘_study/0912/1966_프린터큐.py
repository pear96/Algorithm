import sys
from collections import deque
sys.stdin = open('input.txt')
"""
docs에 문서들을 순서로 넣는데, 기존 index와 함께 넣었다.
그를 위해서 enumerate 함수를 사용했고, iterable 객체를 넣어야해서 우선 list로 만들었다.
그리고 튜플로 만들어진 객체들을 deque에 넣어 앞에서 빼고 뒤에서 넣는걸 빨리 할 수 있도록 했다.

그 후 문서의 중요도를 기준으로 매번 가장 높은 우선순위를 가진 문서를 찾아야 했다.
따라서 max함수를 썼지만 각 튜플의 두 번째 인자로 비교를 해야했다.
그래서 key 라는 인자를 사용했고 lambda로 docs에서 각 docs 요소의 2번째 인자를 return하도록 함수로 만들었다.
https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
그리고 max로 추출된 tuple의 두 번째 인자가 곧 현재 대기열 중 가장 높은 우선순위가 된다.
그를 기준으로 대기열에 문서가 있는 동안 제일 앞의 문서의 뽑아내 우선순위를 파악하여
가장 높은 우선순위일 경우 순서를 1 더하고 아닐 경우 다시 맨 뒤에 추가했다.
그리고 가장 높은 우선순위라서 뽑았는데 마침 내가 원하던 위치의 문서였을 경우
더 이상 볼 필요 없으므로 while 문을 끝내버렸다.
그리고 만약 대기열의 길이가 1일 경우 그냥 계산할 필요가 없으니까
answer = 1로 하고 테스트케이스를 지나갔다.
"""
testcase = int(sys.stdin.readline())  # 테스트 케이스의 수

for tc in range(testcase):
    N, M = map(int, sys.stdin.readline().split())  # N = 문서의 개수, M = 원하는 문서의 현재 위치
    docs = deque(enumerate(list(map(int, sys.stdin.readline().split()))))  # deque(문서 인덱스, 문서 중요도)
    answer = 0

    if len(docs) > 1:  # 문서가 하나면 계산할 필요가 없다.
        while docs: # 대기열에 문서가 있을 때
            first_out = max(docs, key=lambda docs: docs[1])[1] # 최대값을 찾고
            now = docs.popleft()
            if now[1] < first_out:
                docs.append(now)
            else:
                answer += 1
                if now[0] == M:
                    break
    else:
        answer = 1

    print(answer)



