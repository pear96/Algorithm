"""
1208: Flatten
덤핑덤핑 던던댄스~
"""

import sys
sys.stdin = open('1208_input.txt')

# input.txt에 테스트케이스가 없어서 직접 숫자 정해주었습니다.
T = 10

# 덤핑 제한 횟수와 상자 리스트를 받아오는 dump 함수를 만들었습니다.


def dump(dumpings, boxes):
    # 개선하고 싶은 부분인데, 우선 최고-최저 차이를 2로 설정했습니다.
    # 차이가 1 이하이고 덤핑제한횟수를 채웠을 경우 return을 하도록 설정했습니다.
    # 하지만 차이를 for문 초반에 계산할경우 #6번이 계산이 제대로 되지 않습니다.
    # 따라서 우선 초반에 if문에 걸리지 않도록 2로 설정하였습니다.
    dump_gap = 2
    # 덤핑 제한 횟수만큼 반복을 돌고, 반복을 다 돌았는데도 평탄화되지 않았다면
    # for문을 탈출하여최고-최저의 차이를 반환합니다.
    for i in range(dumpings):
        # i == (dumpings -1) 조건은 0까지 갈 수 있는데 1에 걸리는 상황을 막기 위해서입니다.
        if dump_gap <= 1 and i == (dumpings-1):
            return dump_gap
        else:
            # 매 for문을 돌 때마다 sort를 통해 최저값과 최고값의 인덱스를 -1, 0으로 찾아냅니다.
            # 덤핑 작업을 했다면 최고에서 -1, 최저에 +1만큼 높이를 변경합니다.
            boxes[-1] -= 1
            boxes[0] += 1
        # 조건문 다음에 sort와 dump_gap 계산을 해줘야 i가 for문을 빠져나갈 차례에도
        # 연산이 끝난 채로 탈출 할 수 있습니다.
        boxes.sort()
        dump_gap = boxes[-1] - boxes[0]
    # 평탄화가 되지 못한 경우 최고-최저 차이를 반환합니다.
    return dump_gap


for test_case in range(1, T+1):
    dumpings = int(input())
    boxes = list(map(int, input().split()))
    # 우선 초반에 sort를 한 채로 dump함수에 넘겨줍니다.
    boxes.sort()
    answer = dump(dumpings, boxes)
    print(f'#{test_case} {answer}')
