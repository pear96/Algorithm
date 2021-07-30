"""
1206: View
전망 좋은 아파트 구하기~
"""

import sys
sys.stdin = open('1206_input.txt')

# input.txt에 테스트케이스가 없어서 직접 숫자 정해주었습니다.
T = 10

for test_case in range(1, T+1):
    # 아파트의 개수를 받아옵니다 ex)100
    building_count = int(input())
    # 문자열로 입력되어있는 숫자들을 공백으로 나눈뒤, int형으로 바꾸고 그 결과를 list로 만듭니다.
    buildings = list(map(int, input().split()))
    # 답이 될 전망 좋은 세대의 수를 저장할 변수를 초기화 합니다.
    views = 0

    # 아파트 한 동씩 볼 건데, building_count-2는 마지막이 0,0이기 때문에 뒤에서 세번째 까지만 검사할 것이기 때문입니다.
    for i in range(2, building_count-2):
        # 왼쪽 2동, 오른쪽 2동 즉 비교할 대상을 list에 할당하여 초기화합니다.
        compare = [buildings[i-2], buildings[i-1],
                   buildings[i+1], buildings[i+2]]
        # 현재 내가 보는 아파트의 동이 비교 대상보다 클 경우에
        if buildings[i] > max(compare):
            # 비교 대상 중 가장 큰 동과의 차이 만큼을 전망이 좋은 세대로 간주하고 답에 더합니다. 아닐경우 다음 동으로 넘어갑니다.
            views += buildings[i] - max(compare)

    print(f'#{test_case} {views}')
