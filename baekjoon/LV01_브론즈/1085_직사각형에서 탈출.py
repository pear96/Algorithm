import sys

x, y, w, h = map(int, sys.stdin.readline().split())

north = y
south = h - y
east = w - x
west = x

answer = min(north, south, east, west)
print(answer)