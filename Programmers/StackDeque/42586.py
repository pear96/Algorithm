"""
일단 이 문제는 queue로 풀어야 겠네!
progress와 speed 모두 앞부터 나가야하잖아(왼쪽부터)

그러면 하루마다 진행도를 높이면서 숫자를 높이다가, 
(while인가? for로 하려니 마지막날 계산이 안되네)
제일 왼쪽의 요소가 100일 때,
그 뒤의 요소들도 숫자를 계산하고, 
100이면 pop시키면서 count도 늘려야해.
100이 아닌 애를 만나면
다시 하루로 돌아가.
그리고 또 반복해
list에 아무것도 안남을 때 까지

"""
from collections import deque

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
answer = []


def solution(progresses, speeds):
    prg_que = deque(progresses)
    spd_que = deque(speeds)
    count = 0
    while len(prg_que) != 0:
        for i in range(len(prg_que)):
            prg_que[i] += spd_que[i]

        while len(prg_que) != 0 and prg_que[0] >= 100:
            prg_que.popleft()
            spd_que.popleft()
            count += 1

        if count != 0:
            answer.append(count)
        count = 0

    return answer


print(solution(progresses, speeds))
