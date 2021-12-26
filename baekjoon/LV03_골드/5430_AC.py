import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for tc in range(T):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip()
    # 리스트 정제하기
    arr = arr[1:-1]

    if arr:
        arr = list(map(int, arr.split(',')))
    else:
        arr = []
    arr = deque(arr)
    # 리스트 시작 인덱스, 마지막 인덱스
    # s_idx, e_idx = 0, len(arr)-1
    empty = False
    reverse_cnt = 0


    for func in p:
        if func == 'R':
            reverse_cnt += 1
        else:
            if len(arr) == 0:
                empty = True
                break
            else:
                if reverse_cnt % 2:
                    arr.pop()
                else:
                    arr.popleft()
    if empty:
        print('error')
    else:
        print('[', end='')
        if reverse_cnt % 2:
            for idx in range(len(arr)-1, -1, -1):
                if idx == 0:
                    print(arr[idx], end='')
                    break
                print(arr[idx], end=',')
        else:
            for idx in range(len(arr)):
                if idx == len(arr)-1:
                    print(arr[idx], end='')
                    break
                print(arr[idx], end=',')
        print(']')