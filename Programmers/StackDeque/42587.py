from collections import deque

"""
이 문제도 deque로 풀어야해.
왜냐면 앞에서 빼고 뒤에다 더해야하거든
하지만 deque를 써야하는데, location 저장을 어떻게 해야하지?
"""


def solution(priorities, location):
    # 0번째인 경우는 없으므로 정답의 초기값을 1로 설정함
    answer = 1
    # 앞에서 빼고 뒤에서 넣어야하므로 덱 사용
    pri_que = deque(priorities)

    # 값을 반환하면서 중간에 함수를 끄려고 while True
    while True:
        # location이 바라보는 원소가 제일 앞에 있고, 최대값일 경우 계산해온 순서를 반환함.
        # 함수가 끝나는 부분은 여기!
        if location == 0 and pri_que[location] >= max(pri_que):
            return answer

        # 아니라면 지금 제일 앞에있는 애가 최대값을 가졌는지 검사함.
        if pri_que[0] >= max(pri_que):
            pri_que.popleft()
            answer += 1
            # 그렇다면 덱에서 빼버리고 순서를 올린다.(location의 값보다 빨리 나갔으니까)
            # 그런데 location이 양수일 경우 앞에서 빠지면 index를 앞으로 당겨야함.
            if location >= 0:
                location -= 1
        else:
            # 제일 앞이 최대값이 아니라면 앞에서 빼서 뒤로 넣어버림.
            # 그리고 앞에서 하나 사라졌으므로 location도 앞으로 당김.
            pri_que.append(pri_que.popleft())
            location -= 1

        # 하지만 location을 무한히 음수로 계산할 수 없으므로 location의 음수값이 덱의 길이와 같다면 0으로 초기화해줌.
        if abs(location) == len(pri_que):
            location = 0


priorities = [2, 1, 9, 1, 9, 1]
location = 0
print(solution(priorities, location))
