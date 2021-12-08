import sys

up, down, tree = map(int, sys.stdin.readline().split())

day = (tree - down) // (up - down)  # tree에서 down을 빼줘야 낮에 정상에 도착하는 경우를 계산해줄 수 있다.
left = (tree - down) % (up - down)

if left > 0:
    day += 1

print(day)