import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

queue = deque()
queue.append(A)
numbers = dict()
numbers[A] = 1

def bfs():
    while queue:
        number = queue.popleft()

        for next_number in [number * 2, number * 10 + 1]:
            # 어차피 계속 커지잖아.. 그리고 2배가 된게 어차피 짝수인데
            # 서로 방문이 불가능하지않아??? 그러면 visited가 필요 없는건가본데
            if next_number < B:
                # 근데 거기까지 가는 횟수를 어떻게 제대로 세지??
                # 음~ 딕셔너리~ㅎ.. 그니까.. 중간에 필요없는 수들을 다 저장할 수 없으니까...
                numbers[next_number] = numbers[number] + 1
                queue.append(next_number)
            elif next_number == B:
                numbers[B] = numbers[number] + 1
                return numbers[B]
    return -1

print(bfs())