"""
num = 움직여야하는 원반
https://sikaleo.tistory.com/29
"""
import sys

N = int(sys.stdin.readline().rstrip())

K = 1

def hanoi(num, start, sub, goal):
    if num == 1: # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
        print(start, goal)
    else:
        # 원반 n - 1개를 보조 기둥으로 이동(목표 기둥을 보조 기둥으로)
        hanoi(num-1, start, goal, sub)
        # 가장 큰 원반을 목적지로 이동
        print(start, goal)
        # 보조 기둥에 있는 원반 n - 1개를 목적지로 이동(시작 기둥을 보조 기둥으로)
        hanoi(num-1, sub, start, goal)


for i in range(N-1):
    K = K * 2 + 1

print(K)
hanoi(N, 1, 2, 3)