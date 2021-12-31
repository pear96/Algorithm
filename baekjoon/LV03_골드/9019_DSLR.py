"""
BFS
0 ~ 9999까지의 모든 숫자에 대해 visited 배열 생성
step의 숫자가 아니라 (이전 숫자, 사용한 매크로 인덱스)의 튜플 저장
B부터 시작해 A가 될 때까지 역순으로 매크로 방식을 저장하고
reverse해서 출력한다.
아 모야 pypy로 하면 visited에 명령어 쌓아도 되잖아...ㅜㅠㅜㅜㅠㅜㅜㅠ
"""
from collections import deque
T = int(input())
macro = ['D', 'S', 'L', 'R']

for tc in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    visited[A] = [-1]
    found = False
    queue = deque()

    queue.append(A)

    while queue:
        num = queue.popleft()
        if found:
            break

        for i in range(4):
            if i == 0:
                # D
                new_num = 2*num
                if new_num > 9999:
                    new_num %= 10000
            elif i == 1:
                # S
                if num == 0:
                    new_num = 9999
                else:
                    new_num = num - 1
            else:
                d = num
                d1, d = d // 1000, d % 1000
                d2, d = d // 100, d % 100
                d3, d = d // 10, d % 10
                d4 = d
                if i == 2:
                    # L
                    new_num = d2 * 1000 + d3 * 100 + d4 * 10 + d1
                if i == 3:
                    # R
                    new_num = d4 * 1000 + d1 * 100 + d2 * 10 + d3
            if visited[new_num]:
                continue
            visited[new_num] = (num, i)
            # B를 방문했다면 이제 반복 그만
            if new_num == B:
                found = True
                break
            queue.append(new_num)

    answers = []
    now_num = B
    while now_num != A:
        answers.append(macro[visited[now_num][1]])
        now_num = visited[now_num][0]
    answers.reverse()
    print(''.join(answers))
