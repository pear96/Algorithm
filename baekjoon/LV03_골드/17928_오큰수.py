"""
억울해서 잠을 못자겠네
뒤집었다 오른쪽에서 봤다
(값, 인덱스)를 만들었다
별 짓 다했는데
하..............
의욕상실 ㅜ
이래서 알고리즘 문제 풀기가 싫어
그렇게 어려운 발상도 아닌데
왜 나는 이걸 못 푸냐고
왼쪽에서부터 봐도 된다. 중요한 점은 더 큰 숫자가 들어올 때마다 stack을 비워주는 것이다.
그리고 그 stack에는 값이 아니라 index가 들어가야한다.
보고 있는 것과 비교할 것을 빨리 찾기 위하여...
"""
import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
answers = [-1] * N
stack = []

for i in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        popped = stack.pop()
        answers[popped] = numbers[i]
    stack.append(i)

print(' '.join(map(str, answers)))