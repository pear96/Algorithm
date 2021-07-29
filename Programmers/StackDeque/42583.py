"""
다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583

다리 = bridge_length 칸 , weight 무게
트럭 = 1칸, truck_weights무게

다리 = deque

deque의 maxlen을 설정한다.
모든 트럭마다 


"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0]*bridge_length, maxlen=bridge_length)
    trucks = deque(truck_weights)

    while sum(bridge) != 0 and len(trucks) != 0:
        answer += 1
        if (sum(bridge)+trucks[0]) <= weight:
            bridge.append(trucks[0])
            trucks.popleft()
        else:
            bridge.append(0)
            if (sum(bridge)+trucks[0]) <= weight:
                bridge.append(trucks[0])
                trucks.popleft()

    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

solution(bridge_length, weight, truck_weights)
